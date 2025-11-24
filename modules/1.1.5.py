from core.windows_secedit import SeceditModule

class CIS_1_1_5(SeceditModule):
    def __init__(self, config):
        super().__init__(name="CIS 1.1.5 (Complexity)", config=config)
        self.id = "1.1.5"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False):
            return

        # Key in secedit: PasswordComplexity (1 = Enabled, 0 = Disabled)
        target_val = self.config.get(self.id, {}).get('complexity', 1)
        self.apply_secedit_policy("PasswordComplexity", target_val)