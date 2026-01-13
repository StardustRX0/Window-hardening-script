from core.user_rights import UserRightsModule


class CIS_2_2_40(UserRightsModule):
    profiles = ['dc', 'ms']

    profiles = ['dc', 'ms']

    def __init__(self, config):
        super().__init__(name="CIS 2.2.40 (Modify an object label)", config=config)
        self.id = "2.2.40"

    def apply(self):
        # Privilege Constant: SeRelabelPrivilege
        default_users = []
        users = self.config.get(self.id, {}).get('users', default_users)

        self.apply_user_right("SeRelabelPrivilege", users)
