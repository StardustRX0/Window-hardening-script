from core.user_rights import UserRightsModule

class CIS_2_2_44(UserRightsModule):
    def __init__(self, config):
        super().__init__(name="CIS 2.2.44 (Profile System Performance)", config=config)
        self.id = "2.2.44"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return
        
        # Privilege: SeSystemProfilePrivilege
        # CIS Recommendation: Administrators, NT SERVICE\WdiServiceHost
        default_users = ["*S-1-5-32-544", "NT SERVICE\\WdiServiceHost"]
        users = self.config.get(self.id, {}).get('users', default_users)
        
        self.apply_user_right("SeSystemProfilePrivilege", users)