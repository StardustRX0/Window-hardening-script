from core.user_rights import UserRightsModule

class CIS_2_2_28(UserRightsModule):
    def __init__(self, config):
        super().__init__(name="CIS 2.2.28 (Enable delegation)", config=config)
        self.id = "2.2.28"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return
        
        # Privilege: SeEnableDelegationPrivilege
        # CIS Recommendation: Administrators (*S-1-5-32-544)
        users = self.config.get(self.id, {}).get('users', ["*S-1-5-32-544"])
        
        self.apply_user_right("SeEnableDelegationPrivilege", users)