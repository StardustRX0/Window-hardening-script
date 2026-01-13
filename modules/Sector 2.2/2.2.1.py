from core.user_rights import UserRightsModule

class CIS_2_2_1(UserRightsModule):
    profiles = ['dc', 'ms']

    def __init__(self, config):
        super().__init__(name="CIS 2.2.1 (Cred Man Access)", config=config)
        self.id = "2.2.1"

    def apply(self):

        # Privilege: SeTrustedCredManAccessPrivilege
        # Config users should be [] (empty list)
        users = self.config.get(self.id, {}).get('users', [])
        
        self.apply_user_right("SeTrustedCredManAccessPrivilege", users)