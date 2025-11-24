from core.user_rights import UserRightsModule

class CIS_2_2_6(UserRightsModule):
    def __init__(self, config):
        super().__init__(name="CIS 2.2.6 (Memory Quotas)", config=config)
        self.id = "2.2.6"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return
        
        # Privilege: SeIncreaseQuotaPrivilege
        # Recommendation: Administrators, LOCAL SERVICE, NETWORK SERVICE
        defaults = ["*S-1-5-32-544", "*S-1-5-19", "*S-1-5-20"]
        users = self.config.get(self.id, {}).get('users', defaults)
        
        self.apply_user_right("SeIncreaseQuotaPrivilege", users)