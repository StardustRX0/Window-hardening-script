from core.change_table_module import ChangeTableModule


class CIS18_6_8_2(ChangeTableModule):
    """CIS 18.6.8.2 (L1)

    Ensure 'Require Encryption' is set to 'Enabled'.
    """

    id = "18.6.8.2"
    title = "Require Encryption"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\LanmanWorkstation",
            "value_name": "RequireEncryption",
            "value_type": "REG_DWORD",
            "value": 1,
            "label": "Require SMB Encryption (RequireEncryption=1)",
        }
    ]
