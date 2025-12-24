import logging
import subprocess
import re
import os
import shutil
from typing import Any, Dict, List, Optional


class BaseModule:
    def __init__(self, name, config):
        self.name = name
        self.config = config
        self.logger = logging.getLogger(name)

        # NEW: store structured events for JSON export
        self._events: List[Dict[str, Any]] = []

    # -------------------------
    # Event capture helpers
    # -------------------------
    def _record_event(self, result: str, message: str, extra: Optional[Dict[str, Any]] = None) -> None:
        evt = {
            "result": result,   # OK / CHANGED / WARN / ERROR / SKIP
            "message": message,
        }
        if extra:
            evt.update(extra)
        self._events.append(evt)

    def get_events(self, clear: bool = True) -> List[Dict[str, Any]]:
        """Runner calls this after apply()."""
        ev = list(self._events)
        if clear:
            self._events.clear()
        return ev

    # -------------------------
    # Logging (prints + records)
    # -------------------------
    def log_change(self, message):
        self._record_event("CHANGED", message)
        print(f"[CHANGED] [{self.name}]: {message}")

    def log_ok(self, message):
        self._record_event("OK", message)
        print(f"[OK]      [{self.name}]: {message}")

    def log_warn(self, message):
        self._record_event("WARN", message)
        print(f"[WARN]    [{self.name}]: {message}")

    def log_error(self, message):
        self._record_event("ERROR", message)
        print(f"[ERROR]   [{self.name}]: {message}")

    def log_skip(self, message):
        self._record_event("SKIP", message)
        print(f"[SKIP]    [{self.name}]: {message}")

    # -------------------------
    # Existing helpers
    # -------------------------
    def run_command(self, command):
        try:
            result = subprocess.run(
                command, shell=True, check=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            # Keep logger, but also record an event (so runner can export it)
            err = (e.stderr or "").strip()
            self.logger.error(f"Command failed: {err}")
            self.log_error(f"Command failed: {err}")
            return None

    def update_file_content(self, file_path, regex_pattern, replacement_line, backup=True):
        if not os.path.exists(file_path):
            self.log_error(f"File {file_path} not found.")
            return False

        # 1. Read File (Handle Windows UTF-16LE encoding if necessary)
        try:
            with open(file_path, 'r', encoding='utf-16') as f:
                content = f.read()
                encoding = 'utf-16'
        except UnicodeError:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                encoding = 'utf-8'

        # 2. Check if change is needed
        if replacement_line in content:
            self.log_ok(f"Setting '{replacement_line.strip()}' is already set.")
            return False

        # 3. Dry Run Check
        if self.config.get('general', {}).get('dry_run'):
            self.log_change(f"(DRY RUN) Would replace pattern '{regex_pattern}' with '{replacement_line}'")
            return True

        # 4. Create Backup
        if backup:
            shutil.copy2(file_path, f"{file_path}.bak")

        # 5. Perform Regex Substitution
        new_content, count = re.subn(regex_pattern, replacement_line, content, flags=re.MULTILINE)
        if count == 0:
            self.logger.warning(f"Pattern '{regex_pattern}' not found. Appending to end.")
            new_content += f"\n{replacement_line}"

        # 6. Write Back
        with open(file_path, 'w', encoding=encoding) as f:
            f.write(new_content)

        self.log_change(f"Updated file to: {replacement_line.strip()}")
        return True
