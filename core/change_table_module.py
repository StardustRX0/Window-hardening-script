from __future__ import annotations

import os
import re
import tempfile
import uuid
from typing import Any, Dict, List, Optional, Tuple

from core.base_module import BaseModule



class ChangeTableModule(BaseModule):
    """Base class for table-driven CIS modules.

    Instead of writing repetitive apply() logic, each module defines a CHANGES
    list (a small "table") and this base applies them consistently.

    Supported change kinds:
      - secedit_system_access (System Access)
      - secedit_registry      (Registry Values)
      - user_right            (Privilege Rights)

    Dynamic values:
      - value_from: pull a value from this control's config (e.g. "name" or "nested.key")
    """

    # Optional metadata used by the runner and logs
    cis_id: Optional[str] = None
    title: Optional[str] = None
    profiles: Optional[List[str]] = None  # e.g. ["dc"], ["ms"], or ["dc", "ms"]

    # The "table" of changes for this module
    CHANGES: List[Dict[str, Any]] = []

    def __init__(self, config: dict):
        # Prefer CIS id/title if provided
        name = self.cis_id or getattr(self, "id", None) or self.__class__.__name__
        if self.title:
            name = f"{name} ({self.title})"
        super().__init__(name=name, config=config)

        # Back-compat: many modules use self.id
        if self.cis_id and not getattr(self, "id", None):
            self.id = self.cis_id  # type: ignore[attr-defined]

        # Back-compat: some modules use _changes instead of CHANGES
        if (not getattr(self, 'CHANGES', None)) and hasattr(self, '_changes'):
            try:
                self.CHANGES = list(getattr(self, '_changes') or [])
            except Exception:
                # Leave as-is if it's not iterable
                pass


    # ------------------------------------------------------------------
    # Secedit helpers
    # ------------------------------------------------------------------
    @staticmethod
    def _secedit_read_text(path: str) -> Tuple[str, str]:
        """Return (content, encoding) for a secedit-exported INF."""
        try:
            with open(path, "r", encoding="utf-16") as f:
                return f.read(), "utf-16"
        except UnicodeError:
            with open(path, "r", encoding="utf-8") as f:
                return f.read(), "utf-8"

    @staticmethod
    def _secedit_write_text(path: str, content: str, encoding: str) -> None:
        with open(path, "w", encoding=encoding) as f:
            f.write(content)

    @staticmethod
    def _secedit_set_kv_in_section(content: str, key: str, value: str, section: str) -> Tuple[str, bool]:
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
            # Section doesn't exist -> append section at end
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

        # Key not found -> insert before end_idx (end of section)
        lines.insert(end_idx, desired_line)
        return "\n".join(lines) + "\n", True

    def _apply_secedit_kv_batch(self, changes: List[Dict[str, str]]) -> None:
        """Apply multiple secedit key/value changes with a single export/configure."""
        if not changes:
            return

        tmp_dir = tempfile.gettempdir()
        tmp_token = f"secedit-batch-{uuid.uuid4().hex[:8]}"
        temp_cfg = os.path.join(tmp_dir, f"{tmp_token}.inf")
        temp_db = os.path.join(tmp_dir, f"{tmp_token}.sdb")

        try:
            # Export policy to INF
            self.run_command(f'secedit /export /cfg "{temp_cfg}" /quiet')
            if not os.path.exists(temp_cfg):
                self.log_error("Failed to export security policy via secedit.")
                return

            content, encoding = self._secedit_read_text(temp_cfg)

            any_changed = False
            per_change_changed: List[Tuple[Dict[str, str], bool]] = []
            for c in changes:
                key = str(c.get("key", "")).strip()
                val = str(c.get("value", "")).strip()
                section = str(c.get("section", "System Access")).strip() or "System Access"
                label = str(c.get("label") or key).strip()

                if not key:
                    self.log_error("Invalid secedit change: missing 'key'")
                    per_change_changed.append((c, False))
                    continue

                new_content, changed = self._secedit_set_kv_in_section(content, key, val, section)
                content = new_content if changed else content
                any_changed = any_changed or changed
                per_change_changed.append(({
                    "key": key,
                    "value": val,
                    "section": section,
                    "label": label,
                }, changed))

            # Log unchanged as OK
            for info, changed in per_change_changed:
                if not changed:
                    self.log_ok(f"{info['label']} already set in [{info['section']}]")

            if not any_changed:
                return

            # Dry run
            if self.config.get("general", {}).get("dry_run"):
                for info, changed in per_change_changed:
                    if changed:
                        self.log_change(
                            f"(DRY RUN) Would set {info['key']} = {info['value']} in [{info['section']}]"
                        )
                return

            # Write updated INF and configure once
            self._secedit_write_text(temp_cfg, content, encoding)
            self.run_command(f'secedit /configure /db "{temp_db}" /cfg "{temp_cfg}" /quiet')

            for info, changed in per_change_changed:
                if changed:
                    self.log_change(f"Enforced {info['key']} = {info['value']} in [{info['section']}]")

        finally:
            for p in (temp_cfg, temp_db, f"{temp_cfg}.bak"):
                try:
                    if p and os.path.exists(p):
                        os.remove(p)
                except Exception:
                    pass


    def _get_control_cfg(self) -> Optional[Dict[str, Any]]:
        """Return this module's per-control config dict (e.g. config['1.1.1'])."""
        for key in (getattr(self, 'id', None), getattr(self, 'cis_id', None)):
            if isinstance(key, str) and isinstance(self.config.get(key), dict):
                return self.config.get(key)  # type: ignore[return-value]
        return None

    def _resolve_list_from_config(self, path: str, default: Optional[List[str]] = None) -> List[str]:
        """Resolve a list from the module's config section using a dotted path.

        - If missing, returns `default` (or []).
        - If present but not a list, logs an error and returns `default`.
        """
        dflt = list(default or [])
        p = (path or '').strip()
        if not p:
            return dflt

        control_cfg = self._get_control_cfg()
        if not isinstance(control_cfg, dict):
            return dflt

        cur = control_cfg
        for part in p.split('.'):
            if isinstance(cur, dict) and part in cur:
                cur = cur[part]
            else:
                return dflt

        if cur is None:
            return dflt
        if not isinstance(cur, list):
            self.log_error(f"Config value '{p}' must be a list")
            return dflt
        return [str(u) for u in cur]


    def _resolve_value(self, row: Dict[str, Any]) -> Optional[str]:
        """Resolve a row's value.

        Supports:
          - value: literal (string/int/bool)
          - value_from: pull from this control's config, e.g. "name" or "nested.key"

        Optional defaults:
          - default / default_value: used when the config path is missing/empty
          - allow_empty: allow an empty string
        """
        default_val = row.get('default', row.get('default_value'))

        if 'value_from' in row and row.get('value_from') is not None:
            cfg_path = str(row.get('value_from')).strip()
            if not cfg_path:
                self.log_error('Invalid change row: value_from is empty')
                return None

            control_cfg = self._get_control_cfg()
            if not isinstance(control_cfg, dict):
                if default_val is not None:
                    resolved = str(default_val).strip()
                    return str(row.get('value_template') or '{value}').format(value=resolved) if row.get('value_template') is not None else resolved
                self.log_error(f"Missing config section for value_from '{cfg_path}'")
                return None

            cur: Any = control_cfg
            for part in cfg_path.split('.'):
                if isinstance(cur, dict) and part in cur:
                    cur = cur[part]
                else:
                    if default_val is not None:
                        cur = default_val
                        break
                    self.log_error(f"Missing config value '{cfg_path}' (not found at '{part}')")
                    return None

            if cur is None or (isinstance(cur, str) and not cur.strip()):
                if bool(row.get('allow_empty', False)):
                    cur = ''
                elif default_val is not None:
                    cur = default_val
                else:
                    self.log_error(f"Config value '{cfg_path}' is empty")
                    return None

            resolved = str(cur).strip()
            tmpl = row.get('value_template')
            if tmpl is not None:
                try:
                    return str(tmpl).format(value=resolved)
                except Exception as e:
                    self.log_error(f"Invalid value_template for '{cfg_path}': {e}")
                    return None
            return resolved

        v = row.get('value')
        if v is None and 'target_value' in row:
            v = row.get('target_value')
        if v is None:
            if default_val is not None:
                v = default_val
            elif bool(row.get('allow_empty', False)):
                v = ''
            else:
                self.log_error("Invalid change row: missing 'value'")
                return None

        resolved = str(v).strip()
        tmpl = row.get('value_template')
        if tmpl is not None:
            try:
                return str(tmpl).format(value=resolved)
            except Exception as e:
                self.log_error(f"Invalid value_template: {e}")
                return None
        return resolved


    def _build_secedit_changes(self) -> List[Dict[str, str]]:
        """Normalize CHANGES rows into secedit key/value/section records."""
        out: List[Dict[str, str]] = []

        for row in self.CHANGES:
            kind = str(row.get("kind") or row.get("type") or "").strip().lower()

            if kind in ("secedit_system_access", "system_access"):
                val = self._resolve_value(row)
                if val is None:
                    continue
                out.append({
                    "key": str(row.get("key", "")).strip(),
                    "value": val,
                    "section": "System Access",
                    "label": str(row.get("label") or row.get("key") or "").strip(),
                })
                continue

            if kind in ("secedit_registry", "registry_values"):
                val = self._resolve_value(row)
                if val is None:
                    continue
                out.append({
                    "key": str(row.get("key", "")).strip(),
                    "value": val,
                    "section": "Registry Values",
                    "label": str(row.get("label") or row.get("key") or "").strip(),
                })
                continue

            if kind in ("user_right", "privilege_rights", "secedit_privilege_rights"):
                # Right name can be literal or pulled from config
                right = str(row.get("right") or row.get("key") or "").strip()
                if not right:
                    rf = row.get("right_from")
                    if rf:
                        right = str(self._resolve_value({"value_from": rf, "default": row.get("right_default")}) or "").strip()

                if not right:
                    self.log_error("Invalid user_right change: missing 'right'")
                    continue

                users_default = row.get("users_default", [])
                users_list: List[str] = []

                if row.get("users_from") is not None:
                    users_list = self._resolve_list_from_config(str(row.get("users_from")), default=list(users_default) if isinstance(users_default, list) else [])
                else:
                    users = row.get("users")
                    if users is None:
                        users = users_default
                    if isinstance(users, list):
                        users_list = [str(u) for u in users]
                    else:
                        self.log_error(f"Invalid users for {right}: must be a list")
                        users_list = list(users_default) if isinstance(users_default, list) else []

                out.append({
                    "key": right,
                    "value": ",".join(users_list),  # empty => "No One"
                    "section": "Privilege Rights",
                    "label": str(row.get("label") or right).strip(),
                })
                continue

        return out


    def _apply_registry_absent_changes(self) -> None:
        """Ensure registry values are absent (used for CIS 'Not Configured' items)."""
        for row in self.CHANGES:
            kind = str(row.get("kind") or row.get("type") or "").strip().lower()
            if kind not in ("registry_value_absent", "registry_absent", "registry_delete_value"):
                continue

            reg_key = str(row.get("key") or row.get("path") or "").strip()
            value_name = str(row.get("value_name") or row.get("name") or "").strip()
            label = str(row.get("label") or f"{reg_key}:{value_name}").strip()

            if not reg_key or not value_name:
                self.log_error(f"Invalid registry_absent row (missing key/value_name): {row}")
                continue

            # Normalize common forms
            if reg_key.upper().startswith("HKEY_LOCAL_MACHINE"):
                reg_key = "HKLM" + reg_key[len("HKEY_LOCAL_MACHINE"):]
            # Ensure it starts with HKLM\... (reg.exe accepts HKLM\...)
            if reg_key.upper().startswith("HKLM") and not reg_key.upper().startswith("HKLM\\"):
                # If someone passes "HKLMFOO..." or "HKLM:...": normalize to HKLM\FOO...
                rest = reg_key[4:].lstrip("\\").lstrip(":")
                reg_key = "HKLM\\" + rest

            # Check existence without raising/logging errors
            rc, out, err = self.run_command_result(["reg", "query", reg_key, "/v", value_name])
            if rc != 0:
                # Value absent already (compliant)
                continue

            if self.config.get("general", {}).get("dry_run"):
                self.log_change(f"(DRY RUN) Would remove registry value {reg_key}\\{value_name} ({label})")
                continue

            rc2, out2, err2 = self.run_command_result(["reg", "delete", reg_key, "/v", value_name, "/f"])
            if rc2 == 0:
                self.log_change(f"Removed registry value {reg_key}\\{value_name} ({label})")
            else:
                self.log_error(f"Failed to remove registry value {reg_key}\\{value_name}: {err2 or out2}")

    def _parse_reg_dword(self, raw: str) -> Optional[int]:
        raw = (raw or "").strip()
        if not raw:
            return None
        # reg.exe typically returns DWORD as hex (e.g., 0x1) but may return decimal too
        try:
            if raw.lower().startswith("0x"):
                return int(raw, 16)
            # Sometimes reg.exe prints decimal without 0x
            return int(raw)
        except Exception:
            return None

    def _reg_query_value(self, reg_key: str, value_name: str) -> Optional[str]:
        """Return the raw value string from `reg query`, or None if missing."""
        if not reg_key or not value_name:
            return None
        rc, out, err = self.run_command_result(["reg", "query", reg_key, "/v", value_name])
        if rc != 0 or not out:
            return None
        # Parse the value line: <name>  <type>  <data>
        # We search in the whole output to be robust.
        m = re.search(rf"(?im)^{re.escape(value_name)}\s+REG_\w+\s+(.+)$", out)
        if not m:
            return None
        return (m.group(1) or "").strip()

    def _apply_registry_policy_changes(self) -> None:
        """Apply direct registry policy changes (non-secedit)."""
        for row in self.CHANGES:
            kind = str(row.get("kind") or row.get("type") or "").strip().lower()
            if kind not in ("reg_set", "registry_policy", "reg_policy", "registry_set"):
                continue

            reg_key = str(row.get("key") or row.get("path") or "").strip()
            value_name = str(row.get("value_name") or row.get("name") or "").strip()
            reg_type = str(row.get("value_type") or row.get("type") or "REG_DWORD").strip().upper()
            # Normalize common aliases to reg.exe expected types
            reg_type = {
                "DWORD": "REG_DWORD",
                "SZ": "REG_SZ",
                "MULTI_SZ": "REG_MULTI_SZ",
                "EXPAND_SZ": "REG_EXPAND_SZ",
                "QWORD": "REG_QWORD",
                "BINARY": "REG_BINARY",
            }.get(reg_type, reg_type)
            label = str(row.get("label") or f"{reg_key}\\{value_name}").strip()

            target_val = self._resolve_value(row)
            if target_val is None:
                self.log_error(f"Missing value for registry policy change: {label}")
                continue

            current_raw = self._reg_query_value(reg_key, value_name)

            # Compare
            is_match = False
            if reg_type == "REG_DWORD":
                cur_i = self._parse_reg_dword(current_raw or "")
                try:
                    tgt_i = int(str(target_val).strip())
                except Exception:
                    tgt_i = None
                is_match = (cur_i is not None and tgt_i is not None and cur_i == tgt_i)
            else:
                # String / other types: case-insensitive compare
                is_match = (current_raw is not None and str(current_raw).strip().lower() == str(target_val).strip().lower())

            if is_match:
                self.log_ok(f"{label} already set.")
                continue

            if self.config.get("general", {}).get("dry_run"):
                self.log_change(f"(DRY RUN) Would set {label} to {target_val} ({reg_type})")
                continue

            # Ensure key exists and set value
            if reg_type == "REG_DWORD":
                cmd = ["reg", "add", reg_key, "/v", value_name, "/t", reg_type, "/d", str(int(str(target_val).strip())), "/f"]
            else:
                cmd = ["reg", "add", reg_key, "/v", value_name, "/t", reg_type, "/d", str(target_val), "/f"]

            rc2, out2, err2 = self.run_command_result(cmd)
            if rc2 == 0:
                self.log_change(f"Set {label} to {target_val} ({reg_type})")
            else:
                self.log_error(f"Failed to set {label}: {err2 or out2}")

    def _sc_get_start_type(self, svc: str) -> Optional[str]:
        rc, out, err = self.run_command_result(["sc", "qc", svc])
        if rc != 0 or not out:
            return None
        m = re.search(r"START_TYPE\s*:\s*\d+\s+(\S+)", out)
        if not m:
            return None
        token = m.group(1).strip().upper()
        if "DISABLED" in token:
            return "disabled"
        if "AUTO" in token:
            return "auto"
        if "DEMAND" in token or "MANUAL" in token:
            return "manual"
        return token.lower()

    def _sc_get_state(self, svc: str) -> Optional[str]:
        rc, out, err = self.run_command_result(["sc", "query", svc])
        if rc != 0 or not out:
            return None
        m = re.search(r"STATE\s*:\s*\d+\s+(\S+)", out)
        if not m:
            return None
        token = m.group(1).strip().upper()
        if "RUNNING" in token:
            return "running"
        if "STOPPED" in token:
            return "stopped"
        return token.lower()

    def _apply_windows_service_changes(self) -> None:
        """Apply Windows service start/state changes using sc.exe."""
        for row in self.CHANGES:
            kind = str(row.get("kind") or row.get("type") or "").strip().lower()
            if kind not in ("windows_service", "service"):
                continue

            svc = str(row.get("service") or row.get("name") or "").strip()
            if not svc:
                self.log_error("Missing service name in windows_service change")
                continue

            label = str(row.get("label") or f"Service {svc}").strip()
            target_start = str(row.get("startup_type") or row.get("start") or "").strip().lower()
            target_state = str(row.get("state") or "").strip().lower()

            cur_start = self._sc_get_start_type(svc)
            cur_state = self._sc_get_state(svc)

            if cur_start is None and cur_state is None:
                # service likely not installed
                self.log_ok(f"{label}: service not found (OK).")
                continue

            # Normalize targets
            start_map = {
                "disabled": "disabled",
                "disable": "disabled",
                "auto": "auto",
                "automatic": "auto",
                "manual": "manual",
                "demand": "manual",
            }
            target_start_n = start_map.get(target_start, target_start) if target_start else ""
            target_state_n = "stopped" if target_state in ("stop", "stopped") else ("running" if target_state in ("run", "running") else "")

            changes_needed = []
            if target_start_n and cur_start and cur_start != target_start_n:
                changes_needed.append(f"startup_type {cur_start} -> {target_start_n}")
            if target_state_n and cur_state and cur_state != target_state_n:
                changes_needed.append(f"state {cur_state} -> {target_state_n}")

            if not changes_needed:
                self.log_ok(f"{label} already compliant.")
                continue

            if self.config.get("general", {}).get("dry_run"):
                self.log_change(f"(DRY RUN) Would update {label}: {', '.join(changes_needed)}")
                continue

            # Apply changes: stop first if we need to stop
            if target_state_n == "stopped" and cur_state == "running":
                rc, out, err = self.run_command_result(["sc", "stop", svc])
                if rc == 0:
                    self.log_change(f"Stopped {label}")
                else:
                    self.log_error(f"Failed to stop {label}: {err or out}")

            if target_start_n:
                sc_start = {"disabled": "disabled", "auto": "auto", "manual": "demand"}.get(target_start_n, target_start_n)
                rc, out, err = self.run_command_result(["sc", "config", svc, "start=", sc_start])
                if rc == 0:
                    self.log_change(f"Set {label} startup type to {target_start_n}")
                else:
                    self.log_error(f"Failed to set startup type for {label}: {err or out}")

            # Start if needed
            if target_state_n == "running" and cur_state == "stopped":
                rc, out, err = self.run_command_result(["sc", "start", svc])
                if rc == 0:
                    self.log_change(f"Started {label}")
                else:
                    self.log_error(f"Failed to start {label}: {err or out}")




    def _auditpol_setting_string(self, success: bool, failure: bool) -> str:
        if success and failure:
            return "Success and Failure"
        if success and not failure:
            return "Success"
        if failure and not success:
            return "Failure"
        return "No Auditing"

    def _get_auditpol_setting(self, subcategory: str) -> Optional[str]:
        rc, out, err = self.run_command_result(["auditpol", "/get", f"/subcategory:{subcategory}"])
        if rc != 0:
            self.log_error(f"auditpol /get failed for {subcategory}: {err or out}")
            return None

        patterns = ("Success and Failure", "No Auditing", "Success", "Failure")
        found: Optional[str] = None
        for line in (out or "").splitlines():
            line = line.rstrip()
            for p in patterns:
                if re.search(rf"\s{re.escape(p)}\s*$", line):
                    found = p
                    break
        return found

    def _apply_auditpol_changes(self) -> None:
        """Apply Advanced Audit Policy changes using auditpol.exe."""
        for row in self.CHANGES:
            kind = str(row.get("kind") or row.get("type") or "").strip().lower()
            if kind not in ("auditpol", "auditpol_set", "audit_policy", "audit_set"):
                continue

            subcategory = str(
                row.get("subcategory_guid")
                or row.get("subcategory")
                or row.get("guid")
                or row.get("id")
                or ""
            ).strip()
            label = str(row.get("label") or subcategory).strip()

            if not subcategory:
                self.log_error(f"Missing auditpol subcategory for {label}")
                continue

            def _norm_bool(v: Any) -> Optional[bool]:
                if isinstance(v, bool):
                    return v
                if v is None:
                    return None
                s = str(v).strip().lower()
                if s in ("1", "true", "yes", "enable", "enabled", "on"):
                    return True
                if s in ("0", "false", "no", "disable", "disabled", "off"):
                    return False
                return None

            success = _norm_bool(row.get("success"))
            failure = _norm_bool(row.get("failure"))

            # Allow specifying only one side (common in CIS)
            if success is None and failure is None:
                self.log_error(
                    f"Invalid auditpol success/failure for {label} (success={row.get('success')}, failure={row.get('failure')})"
                )
                continue
            if success is None:
                success = False
            if failure is None:
                failure = False

            desired = self._auditpol_setting_string(success, failure)
            current = self._get_auditpol_setting(subcategory)
            if current is None:
                self.log_error(f"Failed to read current audit policy for {label} ({subcategory})")
                continue

            if current == desired:
                self.log_ok(f"{label} already set.")
                continue

            if self.config.get("general", {}).get("dry_run"):
                self.log_change(
                    f"(DRY RUN) Would set audit policy '{label}' ({subcategory}) from '{current}' to '{desired}'"
                )
                continue

            cmd = [
                "auditpol",
                "/set",
                f"/subcategory:{subcategory}",
                f"/success:{'enable' if success else 'disable'}",
                f"/failure:{'enable' if failure else 'disable'}",
            ]
            rc, out, err = self.run_command_result(cmd)
            if rc != 0:
                self.log_error(f"Failed to set audit policy '{label}' ({subcategory}): {err or out}")
                continue

            new_val = self._get_auditpol_setting(subcategory)
            if new_val == desired:
                self.log_change(f"Set audit policy '{label}' ({subcategory}) to '{desired}'")
            else:
                self.log_error(
                    f"Audit policy '{label}' ({subcategory}) did not apply as expected. Current='{new_val}', Desired='{desired}'"
                )

    def apply(self) -> None:
        """Apply all changes listed in CHANGES."""
        secedit_changes = self._build_secedit_changes()
        if secedit_changes:
            self._apply_secedit_kv_batch(secedit_changes)

        # Registry policy (direct registry enforcement)
        self._apply_registry_policy_changes()

        # Windows service configuration
        self._apply_windows_service_changes()

        # Advanced Audit Policy (auditpol.exe)
        self._apply_auditpol_changes()

        # Registry 'Not Configured' enforcement
        self._apply_registry_absent_changes()

        # If there are change kinds we didn't recognize, log a clear error
        for row in self.CHANGES:
            kind = str(row.get("kind") or row.get("type") or "").strip().lower()
            if kind in (
                "secedit_system_access",
                "system_access",
                "secedit_registry",
                "registry_values",
                "user_right",
                "privilege_rights",
                "secedit_privilege_rights",
                "registry_value_absent",
                "registry_absent",
                "registry_delete_value",
                "reg_set",
                "registry_policy",
                "reg_policy",
                "registry_set",
                "windows_service",
                "service",
                "auditpol",
                "auditpol_set",
                "audit_policy",
                "audit_set",
            ):
                continue
            if kind:
                self.log_error(f"Unknown change kind: {kind}")
