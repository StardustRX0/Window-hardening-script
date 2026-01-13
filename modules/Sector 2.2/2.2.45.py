from core.user_rights import UserRightsModule


class CIS_2_2_45(UserRightsModule):
    profiles = ['dc', 'ms']

    profiles = ['dc', 'ms']

    def __init__(self, config):
        super().__init__(name="CIS 2.2.45 (Replace a process level token)", config=config)
        self.id = "2.2.45"

    def apply(self):
        # Privilege Constant: SeAssignPrimaryTokenPrivilege
        default_users = ['*S-1-5-19', '*S-1-5-20']
        users = self.config.get(self.id, {}).get('users', default_users)

        self.apply_user_right("SeAssignPrimaryTokenPrivilege", users)
