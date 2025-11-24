from core.user_rights import UserRightsModule

class CIS_2_2_5(UserRightsModule):
    def __init__(self, config):
        super().__init__(name="CIS 2.2.5 (Add Workstations)", config=config)
        self.id = "2.2.5"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return
        
        # Privilege: SeMachineAccountPrivilege
        # Recommendation: Administrators (*S-1-5-32-544)
        users = self.config.get(self.id, {}).get('users', ["*S-1-5-32-544"])
        self.apply_user_right("SeMachineAccountPrivilege", users)