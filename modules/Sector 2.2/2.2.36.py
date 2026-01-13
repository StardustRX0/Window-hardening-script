from core.user_rights import UserRightsModule

class CIS_2_2_36(UserRightsModule):
    profiles = ['dc', 'ms']

    def __init__(self, config):
        super().__init__(name="CIS 2.2.36 (Lock Pages in Memory)", config=config)
        self.id = "2.2.36"

    def apply(self):

        # Privilege: SeLockMemoryPrivilege
        # Recommendation: No One (Empty list)
        users = self.config.get(self.id, {}).get('users', [])
        self.apply_user_right("SeLockMemoryPrivilege", users)