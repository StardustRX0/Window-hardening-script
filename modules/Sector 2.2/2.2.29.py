from core.user_rights import UserRightsModule


class CIS_2_2_29(UserRightsModule):
    profiles = ['ms']

    profiles = ['ms']

    def __init__(self, config):
        super().__init__(name="CIS 2.2.29 (Enable computer and user accounts to be trusted for delegation)", config=config)
        self.id = "2.2.29"

    def apply(self):
        # Privilege Constant: SeEnableDelegationPrivilege
        default_users = []
        users = self.config.get(self.id, {}).get('users', default_users)

        self.apply_user_right("SeEnableDelegationPrivilege", users)
