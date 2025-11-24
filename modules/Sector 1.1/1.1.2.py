from core.windows_secedit import SeceditModule

class CIS_1_1_2(SeceditModule):
    def __init__(self, config):
        super().__init__(name="CIS 1.1.2 (Max Age)", config=config)
        self.id = "1.1.2"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False):
            return

        # Key in secedit: MaximumPasswordAge
        target_val = self.config.get(self.id, {}).get('max_age', 365)
        self.apply_secedit_policy("MaximumPasswordAge", target_val)