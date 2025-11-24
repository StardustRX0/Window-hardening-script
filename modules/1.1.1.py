from core.windows_secedit import SeceditModule

class CIS_1_1_1(SeceditModule):
    def __init__(self, config):
        super().__init__(name="CIS 1.1.1 (Pass History)", config=config)
        self.id = "1.1.1"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False):
            return

        # Key in secedit: PasswordHistorySize
        target_val = self.config.get(self.id, {}).get('history_count', 24)
        self.apply_secedit_policy("PasswordHistorySize", target_val)