from core.user_rights import UserRightsModule

class CIS_2_2_36(UserRightsModule):
    def __init__(self, config):
        super().__init__(name="CIS 2.2.36 (Lock Pages in Memory)", config=config)
        self.id = "2.2.36"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return
        
        # Privilege: SeLockMemoryPrivilege
        # Recommendation: No One (Empty list)
        users = self.config.get(self.id, {}).get('users', [])
        self.apply_user_right("SeLockMemoryPrivilege", users)