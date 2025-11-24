from core.user_rights import UserRightsModule

class CIS_2_2_7(UserRightsModule):
    def __init__(self, config):
        super().__init__(name="CIS 2.2.7 (Allow Log on Locally)", config=config)
        self.id = "2.2.7"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return
        
        # Privilege: SeInteractiveLogonRight
        # CIS Recommendation (DC): Administrators, ENTERPRISE DOMAIN CONTROLLERS
        default_users = ["*S-1-5-32-544", "*S-1-5-9"]
        users = self.config.get(self.id, {}).get('users', default_users)
        
        self.apply_user_right("SeInteractiveLogonRight", users)