from core.change_table_module import ChangeTableModule


class CIS18_6_8_1(ChangeTableModule):
    """CIS 18.6.8.1 (L1)

    Ensure 'Enable insecure guest logons' is set to 'Disabled'.
    """

    id = "18.6.8.1"
    title = "Enable insecure guest logons"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\LanmanWorkstation",
            "value_name": "AllowInsecureGuestAuth",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "Disable insecure guest logons (AllowInsecureGuestAuth=0)",
        }
    ]
