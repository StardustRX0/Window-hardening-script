from core.user_rights import UserRightsModule


class CIS_2_2_35(UserRightsModule):
    profiles = ['dc', 'ms']

    profiles = ['dc', 'ms']

    def __init__(self, config):
        super().__init__(name="CIS 2.2.35 (Load and unload device drivers)", config=config)
        self.id = "2.2.35"

    def apply(self):
        # Privilege Constant: SeLoadDriverPrivilege
        default_users = ['*S-1-5-32-544']
        users = self.config.get(self.id, {}).get('users', default_users)

        self.apply_user_right("SeLoadDriverPrivilege", users)
