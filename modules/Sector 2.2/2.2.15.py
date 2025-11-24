from core.user_rights import UserRightsModule

class CIS_2_2_15(UserRightsModule):
    def __init__(self, config):
        super().__init__(name="CIS 2.2.15 (Create Token Object)", config=config)
        self.id = "2.2.15"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return
        
        # Privilege: SeCreateTokenPrivilege
        # CIS Recommendation: No One (Empty List)
        users = self.config.get(self.id, {}).get('users', [])
        
        self.apply_user_right("SeCreateTokenPrivilege", users)