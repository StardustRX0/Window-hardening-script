from core.user_rights import UserRightsModule


class CIS_2_2_3(UserRightsModule):
    profiles = ['ms']

    profiles = ['ms']

    def __init__(self, config):
        super().__init__(name="CIS 2.2.3 (Access this computer from the network)", config=config)
        self.id = "2.2.3"

    def apply(self):
        # Privilege Constant: SeNetworkLogonRight
        default_users = ['*S-1-5-32-544', '*S-1-5-11']
        users = self.config.get(self.id, {}).get('users', default_users)

        self.apply_user_right("SeNetworkLogonRight", users)
