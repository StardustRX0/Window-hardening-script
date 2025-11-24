from core.user_rights import UserRightsModule

class CIS_2_2_21(UserRightsModule):
    def __init__(self, config):
        super().__init__(name="CIS 2.2.21 (Deny Network Access)", config=config)
        self.id = "2.2.21"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return
        
        # Privilege: SeDenyNetworkLogonRight
        # CIS Recommendation (DC): Guests
        default_users = ["*S-1-5-32-546"]
        users = self.config.get(self.id, {}).get('users', default_users)
        
        self.apply_user_right("SeDenyNetworkLogonRight", users)