from core.user_rights import UserRightsModule


class CIS_2_2_46(UserRightsModule):
    profiles = ['dc', 'ms']

    profiles = ['dc', 'ms']

    def __init__(self, config):
        super().__init__(name="CIS 2.2.46 (Restore files and directories)", config=config)
        self.id = "2.2.46"

    def apply(self):
        # Privilege Constant: SeRestorePrivilege
        default_users = ['*S-1-5-32-544']
        users = self.config.get(self.id, {}).get('users', default_users)

        self.apply_user_right("SeRestorePrivilege", users)
