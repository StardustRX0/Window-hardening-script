from core.user_rights import UserRightsModule

class CIS_2_2_26(UserRightsModule):
    def __init__(self, config):
        super().__init__(name="CIS 2.2.26 (Deny Remote Interactive Logon)", config=config)
        self.id = "2.2.26"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return
        
        # Privilege: SeDenyRemoteInteractiveLogonRight
        # CIS Recommendation (DC): Guests
        default_users = ["*S-1-5-32-546"]
        users = self.config.get(self.id, {}).get('users', default_users)
        
        self.apply_user_right("SeDenyRemoteInteractiveLogonRight", users)