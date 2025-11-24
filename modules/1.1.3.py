from core.windows_secedit import SeceditModule

class CIS_1_1_3(SeceditModule):
    def __init__(self, config):
        super().__init__(name="CIS 1.1.3 (Min Age)", config=config)
        self.id = "1.1.3"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False):
            return

        # Key in secedit: MinimumPasswordAge
        target_val = self.config.get(self.id, {}).get('min_age', 1)
        self.apply_secedit_policy("MinimumPasswordAge", target_val)