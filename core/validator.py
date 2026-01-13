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
        # Ensure the 'general' section exists
        if 'general' not in self.config:
            self.errors.append("Missing 'general' section in config.yaml")
        else:
            # Check if 'dry_run' is a boolean (True/False)
            self._check_type('general', 'dry_run', bool)

            # Optional: profile selector ("dc" or "ms")
            if "profile" in self.config.get("general", {}):
                prof = self.config["general"].get("profile")
                if not isinstance(prof, str):
                    self.errors.append(
                        f"In 'general': 'profile' must be a string (dc/ms), got {type(prof).__name__}"
                    )
                else:
                    p = prof.strip().lower()
                    aliases = {
                        "domain controller": "dc",
                        "domain_controller": "dc",
                        "dc": "dc",
                        "member server": "ms",
                        "member_server": "ms",
                        "ms": "ms",
                    }
                    if p not in aliases:
                        self.errors.append(
                            "In 'general': 'profile' must be one of: dc, ms (or 'domain controller', 'member server')"
                        )

        # Basic checks for control sections
        for key, val in (self.config or {}).items():
            if key == "general":
                continue
            if not isinstance(val, dict):
                self.errors.append(f"Control '{key}' must be a mapping/dict, got {type(val).__name__}")
                continue

            if "enabled" in val and not isinstance(val["enabled"], bool):
                self.errors.append(
                    f"In '{key}': 'enabled' must be bool, got {type(val['enabled']).__name__}"
                )

            if "users" in val:
                if not isinstance(val["users"], list) or any(not isinstance(u, str) for u in val["users"]):
                    self.errors.append(f"In '{key}': 'users' must be a list of strings")

            # Optional per-control profile gate
            if "profiles" in val:
                profiles = val.get("profiles")
                if not isinstance(profiles, list) or any(not isinstance(p, str) for p in profiles):
                    self.errors.append(f"In '{key}': 'profiles' must be a list of strings (dc/ms)")
            if "profile" in val:
                profile = val.get("profile")
                if not isinstance(profile, str):
                    self.errors.append(f"In '{key}': 'profile' must be a string (dc/ms)")

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