from core.user_rights import UserRightsModule

class CIS_2_2_17(UserRightsModule):
    profiles = ['dc', 'ms']

    def __init__(self, config):
        super().__init__(name="CIS 2.2.17 (Shared Objects)", config=config)
        self.id = "2.2.17   "

    def apply(self):

        # Privilege: SeCreatePermanentPrivilege
        # Recommendation: No One (Empty list)
        users = self.config.get(self.id, {}).get('users', [])
        self.apply_user_right("SeCreatePermanentPrivilege", users)