from core.user_rights import UserRightsModule

class CIS_2_2_2(UserRightsModule):
    def __init__(self, config):
        super().__init__(name="CIS 2.2.2 (Network Access)", config=config)
        self.id = "2.2.2"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return

        # Privilege Constant: SeNetworkLogonRight
        # Recommendation: Administrators, Authenticated Users, ENTERPRISE DOMAIN CONTROLLERS
        default_users = ["*S-1-5-32-544", "*S-1-5-11", "*S-1-5-9"]
        users = self.config.get(self.id, {}).get('users', default_users)
        
        self.apply_user_right("SeNetworkLogonRight", users)