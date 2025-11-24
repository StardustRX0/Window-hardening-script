from core.windows_secedit import SeceditModule

class CIS_1_1_7(SeceditModule):
    def __init__(self, config):
        super().__init__(name="CIS 1.1.7 (Reversible Enc)", config=config)
        self.id = "1.1.7"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False):
            return

        # Key in secedit: ClearTextPassword (0 = Disabled)
        target_val = self.config.get(self.id, {}).get('reversible', 0)
        self.apply_secedit_policy("ClearTextPassword", target_val)