import os
from core.base_module import BaseModule

class SeceditModule(BaseModule):
    def apply_secedit_policy(self, key_name, target_value, section_name="System Access"):
        """
        Generic logic to update Windows Security Policy via secedit.
        """
        temp_cfg = f"C:\\Windows\\Temp\\{self.id}.inf"
        
        # 1. Export Policy
        self.run_command(f"secedit /export /cfg {temp_cfg} /quiet")
        
        if not os.path.exists(temp_cfg):
            self.logger.error("Failed to export security policy.")
            return

        # 2. Define Regex Pattern to find the specific key
        # Pattern looks for: KeyName = Value
        pattern = f"^\\s*{key_name}\\s*=\s*(-?\d+)"
        replacement = f"{key_name} = {target_value}"

        # 3. Update Content using the BaseModule's regex engine
        # Note: secedit files are usually UTF-16
        changed = self.update_file_content(temp_cfg, pattern, replacement)

        # 4. Apply Changes
        if changed and not self.config.get('general', {}).get('dry_run'):
            self.run_command(f"secedit /configure /db secedit.sdb /cfg {temp_cfg} /quiet")
            self.log_change(f"Enforced {key_name} to {target_value}")
        
        # Cleanup
        if os.path.exists(temp_cfg): os.remove(temp_cfg)
        if os.path.exists(f"{temp_cfg}.bak"): os.remove(f"{temp_cfg}.bak")