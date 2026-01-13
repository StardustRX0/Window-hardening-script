from core.user_rights import UserRightsModule

class CIS_2_2_43(UserRightsModule):
    profiles = ['dc', 'ms']

    def __init__(self, config):
        # FIXED: Updated name to match the actual rule
        super().__init__(name="CIS 2.2.43 (Profile single process)", config=config)
        self.id = "2.2.43"

    def apply(self):

        # Privilege: SeProfileSingleProcessPrivilege (Profile single process)
        # CIS Recommendation: Administrators (*S-1-5-32-544)
        users = self.config.get(self.id, {}).get('users', ["*S-1-5-32-544"])
        
        self.apply_user_right("SeProfileSingleProcessPrivilege", users)