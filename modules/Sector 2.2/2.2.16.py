from core.user_rights import UserRightsModule

class CIS_2_2_16(UserRightsModule):
    def __init__(self, config):
        super().__init__(name="CIS 2.2.16 (Create Global Objects)", config=config)
        self.id = "2.2.16"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return

        # Privilege Constant: SeCreateGlobalPrivilege
        # Recommendation: Administrators, LOCAL SERVICE, NETWORK SERVICE, SERVICE
        default_users = ["*S-1-5-32-544", "*S-1-5-19", "*S-1-5-20", "*S-1-5-6"]
        
        users = self.config.get(self.id, {}).get('users', default_users)
        
        self.apply_user_right("SeCreateGlobalPrivilege", users)