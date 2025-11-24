from core.user_rights import UserRightsModule

class CIS_2_2_1(UserRightsModule):
    def __init__(self, config):
        super().__init__(name="CIS 2.2.1 (Cred Man Access)", config=config)
        self.id = "2.2.1"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return
        
        # Privilege: SeTrustedCredManAccessPrivilege
        # Config users should be [] (empty list)
        users = self.config.get(self.id, {}).get('users', [])
        
        self.apply_user_right("SeTrustedCredManAccessPrivilege", users)