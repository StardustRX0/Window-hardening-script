from core.change_table_module import ChangeTableModule


class CIS_18_5_9(ChangeTableModule):
    """18.5.9 Ensure 'MSS: (ScreenSaverGracePeriod) The time in seconds before the screen saver grace period expires'."""

    cis_id = "18.5.9"
    title = "MSS (ScreenSaverGracePeriod) Screen saver grace period (seconds)"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",
            "value_name": "ScreenSaverGracePeriod",
            "value_type": "REG_SZ",
            "value": "5",
            "label": "Set screen saver grace period to 5 seconds (ScreenSaverGracePeriod=5)",
        },
    ]
