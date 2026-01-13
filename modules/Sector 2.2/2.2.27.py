from core.user_rights import UserRightsModule


class CIS_2_2_27(UserRightsModule):
    profiles = ['ms']

    profiles = ['ms']

    def __init__(self, config):
        super().__init__(name="CIS 2.2.27 (Deny log on through Remote Desktop Services)", config=config)
        self.id = "2.2.27"

    def apply(self):
        # Privilege Constant: SeDenyRemoteInteractiveLogonRight
        default_users = ['*S-1-5-32-546', '*S-1-5-113']
        users = self.config.get(self.id, {}).get('users', default_users)

        self.apply_user_right("SeDenyRemoteInteractiveLogonRight", users)
