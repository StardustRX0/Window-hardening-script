from core.windows_secedit import SeceditModule

class CIS_1_2_4(SeceditModule):
    def __init__(self, config):
        super().__init__(name="CIS 1.2.4 (Reset Lockout)", config=config)
        self.id = "1.2.4"

    def apply(self):
        if not self.config.get(self.id, {}).get('enabled', False): return

        # Key: ResetLockoutCount. Value is in minutes.
        val = self.config.get(self.id, {}).get('reset_after', 15)
        self.apply_secedit_policy("ResetLockoutCount", val)