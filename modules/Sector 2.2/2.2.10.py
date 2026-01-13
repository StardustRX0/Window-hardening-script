from core.user_rights import UserRightsModule


class CIS_2_2_10(UserRightsModule):
    profiles = ['ms']

    profiles = ['ms']

    def __init__(self, config):
        super().__init__(name="CIS 2.2.10 (Allow log on through Remote Desktop Services)", config=config)
        self.id = "2.2.10"

    def apply(self):
        # Privilege Constant: SeRemoteInteractiveLogonRight
        default_users = ['*S-1-5-32-544', '*S-1-5-32-555']
        users = self.config.get(self.id, {}).get('users', default_users)

        self.apply_user_right("SeRemoteInteractiveLogonRight", users)
