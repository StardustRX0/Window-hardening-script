import logging

logger = logging.getLogger("Validator")

class ConfigValidator:
    def __init__(self, config):
        self.config = config
        self.errors = []

    def validate(self):
        """
        Main entry point. Returns True if config is good, False if bad.
        """
        # Example Check: Ensure the 'general' section exists
        if 'general' not in self.config:
            self.errors.append("Missing 'general' section in config.yaml")
        else:
            # Check if 'dry_run' is a boolean (True/False)
            self._check_type('general', 'dry_run', bool)

        # --- Final Decision ---
        if self.errors:
            for e in self.errors:
                logger.error(f"[CONFIG ERROR] {e}")
            return False # Validation Failed
        
        return True # Validation Passed

    def _check_type(self, section, key, expected_type):
        """Reusable helper to check data types"""
        if section in self.config and key in self.config[section]:
            value = self.config[section][key]
            if not isinstance(value, expected_type):
                self.errors.append(
                    f"In '{section}': '{key}' must be {expected_type.__name__}, got {type(value).__name__}"
                )