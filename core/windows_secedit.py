import os
import re
import tempfile
import uuid
from typing import Tuple

from core.base_module import BaseModule


class SeceditModule(BaseModule):
    """Helpers for settings that are applied via secedit (Local Security Policy).

    Key fix vs previous version:
    - If the key is missing, we insert it **inside the correct INF section** (not append to EOF).
    - We write the secedit database to a unique file in %TEMP% and clean it up.
    - We avoid duplicate "CHANGED" events for the same setting.
    """

    def _read_text(self, path: str) -> Tuple[str, str]:
        """Return (content, encoding)."""
        try:
            with open(path, "r", encoding="utf-16") as f:
                return f.read(), "utf-16"
        except UnicodeError:
            with open(path, "r", encoding="utf-8") as f:
                return f.read(), "utf-8"

    def _write_text(self, path: str, content: str, encoding: str) -> None:
        with open(path, "w", encoding=encoding) as f:
            f.write(content)

    def _set_kv_in_section(self, content: str, key: str, value: str, section: str) -> Tuple[str, bool]:
        """Set `key = value` within [section]. Returns (new_content, changed)."""
        desired_line = f"{key} = {value}".rstrip()

        # Normalize newlines
        lines = content.splitlines()

        # Find section header
        section_re = re.compile(rf"^\s*\[{re.escape(section)}\]\s*$", re.IGNORECASE)
        header_idx = None
        for i, line in enumerate(lines):
            if section_re.match(line):
                header_idx = i
                break

        if header_idx is None:
            # Section doesn't exist → append section at end
            if lines and lines[-1].strip() != "":
                lines.append("")
            lines.extend([f"[{section}]", desired_line])
            return "\n".join(lines) + "\n", True

        # Determine section bounds: from header_idx+1 to next [Section] or EOF
        end_idx = len(lines)
        next_section_re = re.compile(r"^\s*\[.*\]\s*$")
        for j in range(header_idx + 1, len(lines)):
            if next_section_re.match(lines[j]):
                end_idx = j
                break

        # Look for existing key within section
        key_re = re.compile(rf"^\s*{re.escape(key)}\s*=\s*(.*)$", re.IGNORECASE)
        for j in range(header_idx + 1, end_idx):
            m = key_re.match(lines[j])
            if not m:
                continue

            current_line = f"{key} = {m.group(1).strip()}".rstrip()
            if current_line == desired_line:
                return content, False

            lines[j] = desired_line
            return "\n".join(lines) + "\n", True

        # Key not found → insert before end_idx (end of section)
        lines.insert(end_idx, desired_line)
        return "\n".join(lines) + "\n", True

    def apply_secedit_policy(self, key_name: str, target_value: str, section_name: str = "System Access"):
        """Export current policy to a temp INF, edit it, and configure it back."""
        tmp_dir = tempfile.gettempdir()
        tmp_token = f"{getattr(self, 'id', 'secedit')}-{uuid.uuid4().hex[:8]}"
        temp_cfg = os.path.join(tmp_dir, f"{tmp_token}.inf")
        temp_db = os.path.join(tmp_dir, f"{tmp_token}.sdb")

        try:
            # 1) Export policy
            self.run_command(f'secedit /export /cfg "{temp_cfg}" /quiet')
            if not os.path.exists(temp_cfg):
                self.log_error("Failed to export security policy via secedit.")
                return

            # 2) Read + edit within correct section
            content, encoding = self._read_text(temp_cfg)
            new_content, changed = self._set_kv_in_section(content, key_name, target_value, section_name)

            if not changed:
                self.log_ok(f"{key_name} already set to {target_value} in [{section_name}].")
                return

            # 3) Dry run
            if self.config.get("general", {}).get("dry_run"):
                self.log_change(f"(DRY RUN) Would set {key_name} = {target_value} in [{section_name}]")
                return

            # 4) Write INF and configure
            self._write_text(temp_cfg, new_content, encoding)
            self.run_command(f'secedit /configure /db "{temp_db}" /cfg "{temp_cfg}" /quiet')
            self.log_change(f"Enforced {key_name} = {target_value} in [{section_name}]")

        finally:
            # Cleanup (best-effort)
            for p in (temp_cfg, temp_db, f"{temp_cfg}.bak"):
                try:
                    if p and os.path.exists(p):
                        os.remove(p)
                except Exception:
                    pass

    # ------------------------------------------------------------------
    # New: table-driven wrappers (batch apply)
    # ------------------------------------------------------------------
    @staticmethod
    def apply_kv_batch(
        module: BaseModule,
        changes: list[dict],
    ) -> None:
        """Apply multiple secedit key/value changes with a single export/configure.

        Each change dict supports:
          - key (str)
          - value (str)
          - section (str)  # e.g. "System Access", "Privilege Rights", "Registry Values"
          - label (str)    # optional, for nicer logs
        """

        if not changes:
            return

        tmp_dir = tempfile.gettempdir()
        tmp_token = f"secedit-batch-{uuid.uuid4().hex[:8]}"
        temp_cfg = os.path.join(tmp_dir, f"{tmp_token}.inf")
        temp_db = os.path.join(tmp_dir, f"{tmp_token}.sdb")

        try:
            module.run_command(f'secedit /export /cfg "{temp_cfg}" /quiet')
            if not os.path.exists(temp_cfg):
                module.log_error("Failed to export security policy via secedit.")
                return

            # Read INF
            try:
                with open(temp_cfg, "r", encoding="utf-16") as f:
                    content = f.read()
                    encoding = "utf-16"
            except UnicodeError:
                with open(temp_cfg, "r", encoding="utf-8") as f:
                    content = f.read()
                    encoding = "utf-8"

            # Apply changes in-memory
            any_changed = False
            per_change_changed: list[tuple[dict, bool]] = []
            for c in changes:
                key = str(c.get("key", "")).strip()
                val = str(c.get("value", "")).strip()
                section = str(c.get("section", "System Access")).strip() or "System Access"
                label = str(c.get("label") or key).strip()

                if not key:
                    module.log_error("Invalid secedit change: missing 'key'")
                    per_change_changed.append((c, False))
                    continue

                # Reuse instance helper by creating a lightweight SeceditModule-like helper
                helper = SeceditModule.__new__(SeceditModule)  # bypass __init__
                # Call the pure method using our current content
                new_content, changed = helper._set_kv_in_section(content, key, val, section)
                content = new_content if changed else content
                any_changed = any_changed or changed
                per_change_changed.append(({
                    "key": key,
                    "value": val,
                    "section": section,
                    "label": label,
                }, changed))

            # Log unchanged ones as OK
            for info, changed in per_change_changed:
                if not changed:
                    module.log_ok(f"{info['label']} already set in [{info['section']}]")

            if not any_changed:
                return

            # Dry run
            if module.config.get("general", {}).get("dry_run"):
                for info, changed in per_change_changed:
                    if changed:
                        module.log_change(
                            f"(DRY RUN) Would set {info['key']} = {info['value']} in [{info['section']}]"
                        )
                return

            # Write + configure once
            with open(temp_cfg, "w", encoding=encoding) as f:
                f.write(content)
            module.run_command(f'secedit /configure /db "{temp_db}" /cfg "{temp_cfg}" /quiet')

            for info, changed in per_change_changed:
                if changed:
                    module.log_change(f"Enforced {info['key']} = {info['value']} in [{info['section']}]")

        finally:
            for p in (temp_cfg, temp_db, f"{temp_cfg}.bak"):
                try:
                    if p and os.path.exists(p):
                        os.remove(p)
                except Exception:
                    pass
