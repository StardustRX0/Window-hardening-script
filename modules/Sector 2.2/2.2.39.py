from core.user_rights import UserRightsModule


class CIS_2_2_39(UserRightsModule):
    profiles = ['ms']

    profiles = ['ms']

    def __init__(self, config):
        super().__init__(name="CIS 2.2.39 (Manage auditing and security log)", config=config)
        self.id = "2.2.39"

    def apply(self):
        # Privilege Constant: SeSecurityPrivilege
        default_users = ['*S-1-5-32-544']
        users = self.config.get(self.id, {}).get('users', default_users)

        self.apply_user_right("SeSecurityPrivilege", users)
