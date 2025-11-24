from core.user_rights import UserRightsModule

class CIS_2_2_25(UserRightsModule):
    def __init__(self, config):
        super().__init__(name="CIS 2.2.25 (Deny Interactive Logon)", config=config)
        self.id = "2.2.25"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return
        
        # Privilege: SeDenyInteractiveLogonRight
        # CIS Recommendation (DC): Guests
        default_users = ["*S-1-5-32-546"]
        users = self.config.get(self.id, {}).get('users', default_users)
        
        self.apply_user_right("SeDenyInteractiveLogonRight", users)