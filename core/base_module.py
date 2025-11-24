import logging
import subprocess
import re
import os
import shutil

class BaseModule:
    def __init__(self, name, config):
        self.name = name
        self.config = config
        self.logger = logging.getLogger(name)

    def run_command(self, command):
        """Run shell commands (Linux) or PowerShell/CMD (Windows)"""
        try:
            result = subprocess.run(
                command, shell=True, check=True, 
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Command failed: {e.stderr}")
            return None

    def update_file_content(self, file_path, regex_pattern, replacement_line, backup=True):
        if not os.path.exists(file_path):
            self.logger.error(f"File {file_path} not found.")
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
        # We use re.search to see if the *current* state matches the *desired* state
        # If the replacement line is already exactly present, do nothing.
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
        # flags=re.MULTILINE ensures ^ and $ work on each line
        new_content, count = re.subn(regex_pattern, replacement_line, content, flags=re.MULTILINE)

        # If no match found, we might need to append (depending on policy). 
        # For this example, we assume the key exists and just needs updating.
        if count == 0:
            self.logger.warning(f"Pattern '{regex_pattern}' not found. Appending to end.")
            new_content += f"\n{replacement_line}"

        # 6. Write Back
        with open(file_path, 'w', encoding=encoding) as f:
            f.write(new_content)
        
        self.log_change(f"Updated file to: {replacement_line.strip()}")
        return True

    def log_change(self, message):
        print(f"[CHANGED] [{self.name}]: {message}")

    def log_ok(self, message):
        print(f"[OK]      [{self.name}]: {message}")