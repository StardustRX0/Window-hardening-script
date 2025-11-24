from core.windows_secedit import SeceditModule

class CIS_1_2_1(SeceditModule):
    def __init__(self, config):
        super().__init__(name="CIS 1.2.1 (Lockout Duration)", config=config)
        self.id = "1.2.1"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return

        # Key: LockoutDuration. Value is in minutes.
        val = self.config.get(self.id, {}).get('duration', 15)
        self.apply_secedit_policy("LockoutDuration", val)