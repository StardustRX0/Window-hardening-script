from core.user_rights import UserRightsModule

class CIS_2_2_4(UserRightsModule):
    def __init__(self, config):
        super().__init__(name="CIS 2.2.4 (Act as OS)", config=config)
        self.id = "2.2.4"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return
        
        # Privilege: SeTcbPrivilege
        users = self.config.get(self.id, {}).get('users', [])
        
        self.apply_user_right("SeTcbPrivilege", users)