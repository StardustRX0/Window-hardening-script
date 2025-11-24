from core.windows_secedit import SeceditModule

class CIS_1_1_4(SeceditModule):
    def __init__(self, config):
        super().__init__(name="CIS 1.1.4 (Min Length)", config=config)
        self.id = "1.1.4"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False):
            return

        # Key in secedit: MinimumPasswordLength
        target_val = self.config.get(self.id, {}).get('min_length', 14)
        self.apply_secedit_policy("MinimumPasswordLength", target_val)