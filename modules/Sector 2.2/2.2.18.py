from core.user_rights import UserRightsModule

class CIS_2_2_18(UserRightsModule):
    profiles = ['dc']

    def __init__(self, config):
        super().__init__(name="CIS 2.2.18 (Create symbolic links)", config=config)
        self.id = "2.2.18"

    def apply(self):

        # Privilege: SeCreateSymbolicLinkPrivilege (Create symbolic links)
        # CIS Recommendation: Administrators (*S-1-5-32-544)
        users = self.config.get(self.id, {}).get('users', ["*S-1-5-32-544"])
        
        self.apply_user_right("SeCreateSymbolicLinkPrivilege", users)