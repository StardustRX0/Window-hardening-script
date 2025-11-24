from core.user_rights import UserRightsModule

class CIS_2_2_30(UserRightsModule):
    def __init__(self, config):
        # FIXED: Updated name to match the actual rule
        super().__init__(name="CIS 2.2.30 (Shut down the system)", config=config)
        self.id = "2.2.30"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return
        
        # Privilege: SeRemoteShutdownPrivilege (Shut down the system)
        # CIS Recommendation: Administrators (*S-1-5-32-544)
        users = self.config.get(self.id, {}).get('users', ["*S-1-5-32-544"])
        
        self.apply_user_right("SeRemoteShutdownPrivilege", users)