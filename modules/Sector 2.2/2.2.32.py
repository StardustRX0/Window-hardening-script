from core.user_rights import UserRightsModule


class CIS_2_2_32(UserRightsModule):
    profiles = ['dc']

    profiles = ['dc']

    def __init__(self, config):
        super().__init__(name="CIS 2.2.32 (Impersonate a client after authentication)", config=config)
        self.id = "2.2.32"

    def apply(self):
        # Privilege Constant: SeImpersonatePrivilege
        default_users = ['*S-1-5-32-544', '*S-1-5-19', '*S-1-5-20', '*S-1-5-6']
        users = self.config.get(self.id, {}).get('users', default_users)

        self.apply_user_right("SeImpersonatePrivilege", users)
