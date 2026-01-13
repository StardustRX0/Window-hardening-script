from core.user_rights import UserRightsModule


class CIS_2_2_34(UserRightsModule):
    profiles = ['dc', 'ms']

    profiles = ['dc', 'ms']

    def __init__(self, config):
        super().__init__(name="CIS 2.2.34 (Increase scheduling priority)", config=config)
        self.id = "2.2.34"

    def apply(self):
        # Privilege Constant: SeIncreaseBasePriorityPrivilege
        default_users = ['*S-1-5-32-544', 'Window Manager\\Window Manager Group']
        users = self.config.get(self.id, {}).get('users', default_users)

        self.apply_user_right("SeIncreaseBasePriorityPrivilege", users)
