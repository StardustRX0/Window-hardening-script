from core.user_rights import UserRightsModule


class CIS_2_2_22(UserRightsModule):
    profiles = ['ms']

    profiles = ['ms']

    def __init__(self, config):
        super().__init__(name="CIS 2.2.22 (Deny access to this computer from the network)", config=config)
        self.id = "2.2.22"

    def apply(self):
        # Privilege Constant: SeDenyNetworkLogonRight
        default_users = ['*S-1-5-32-546', '*S-1-5-114']
        users = self.config.get(self.id, {}).get('users', default_users)

        self.apply_user_right("SeDenyNetworkLogonRight", users)
