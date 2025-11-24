from core.base_module import BaseModule

class CIS_1_2_3(BaseModule):
    def __init__(self, config):
        super().__init__(name="CIS 1.2.3 (Admin Lockout)", config=config)
        self.id = "1.2.3"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return
            
        key = r"HKLM\SYSTEM\CurrentControlSet\Control\Lsa"
        val_name = "AllowAdministratorLockout"
        target_data = str(self.config.get(self.id, {}).get('admin_lockout', 1))

        # Check using reg query
        res = self.run_command(f'reg query "{key}" /v {val_name}')
        
        if res and f"0x{target_data}" in res:
             self.log_ok("Administrator Lockout is already enabled.")
        else:
             if not self.config.get('general', {}).get('dry_run'):
                 self.run_command(f'reg add "{key}" /v {val_name} /t REG_DWORD /d {target_data} /f')
                 self.log_change("Enabled Administrator Lockout in Registry")
             else:
                 self.log_change("(DRY RUN) Would enable Administrator Lockout")