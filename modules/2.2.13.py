from core.user_rights import UserRightsModule

class CIS_2_2_13(UserRightsModule):
    def __init__(self, config):
        super().__init__(name="CIS 2.2.13 (Time Zone)", config=config)
        self.id = "2.2.13"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return
        
        # Privilege: SeTimeZonePrivilege
        # Recommendation: Administrators, LOCAL SERVICE
        defaults = ["*S-1-5-32-544", "*S-1-5-19"]
        users = self.config.get(self.id, {}).get('users', defaults)
        
        self.apply_user_right("SeTimeZonePrivilege", users)