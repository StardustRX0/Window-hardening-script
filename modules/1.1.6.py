from core.base_module import BaseModule

class CIS_1_1_6(BaseModule):
    def __init__(self, config):
        super().__init__(name="CIS 1.1.6 (Relax Limits)", config=config)
        self.id = "1.1.6"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False):
            return
            
        # This is a Registry Setting
        # Key: HKLM\SYSTEM\CurrentControlSet\Control\SAM
        # Value: RelaxMinimumPasswordLengthLimits (DWORD) -> 1
        
        key = r"HKLM\SYSTEM\CurrentControlSet\Control\SAM"
        val_name = "RelaxMinimumPasswordLengthLimits"
        target_data = "1"

        # Check current state using 'reg query'
        check_cmd = f'reg query "{key}" /v {val_name}'
        current_val = self.run_command(check_cmd)
        
        # Logic to check if update is needed
        # Output usually looks like: RelaxMinimumPasswordLengthLimits    REG_DWORD    0x1
        if current_val and "0x1" in current_val:
             self.log_ok("Relax limits already enabled.")
        else:
             if not self.config.get('general', {}).get('dry_run'):
                 cmd = f'reg add "{key}" /v {val_name} /t REG_DWORD /d {target_data} /f'
                 self.run_command(cmd)
                 self.log_change("Enabled RelaxMinimumPasswordLengthLimits in Registry")
             else:
                 self.log_change("(DRY RUN) Would enable RelaxMinimumPasswordLengthLimits")