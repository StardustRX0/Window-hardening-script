from core.windows_secedit import SeceditModule

class CIS_1_2_2(SeceditModule):
    def __init__(self, config):
        super().__init__(name="CIS 1.2.2 (Lockout Threshold)", config=config)
        self.id = "1.2.2"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return

        # Key: LockoutBadCount. Value is number of attempts.
        val = self.config.get(self.id, {}).get('threshold', 5)
        self.apply_secedit_policy("LockoutBadCount", val)