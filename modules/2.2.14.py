from core.user_rights import UserRightsModule

class CIS_2_2_14(UserRightsModule):
    def __init__(self, config):
        # FIXED: Updated name to match the actual rule
        super().__init__(name="CIS 2.2.14 (Create a pagefile)", config=config)
        self.id = "2.2.14"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return
        
        # Privilege: SeCreatePagefilePrivilege (Create a pagefile)
        # CIS Recommendation: Administrators (*S-1-5-32-544)
        users = self.config.get(self.id, {}).get('users', ["*S-1-5-32-544"])
        
        self.apply_user_right("SeCreatePagefilePrivilege", users)