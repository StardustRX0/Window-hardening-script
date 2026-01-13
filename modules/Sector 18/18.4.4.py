from core.change_table_module import ChangeTableModule


class CIS_18_4_4(ChangeTableModule):
    """18.4.4 Ensure 'Enable Certificate Padding'."""

    cis_id = "18.4.4"
    title = "Enable Certificate Padding"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "reg_set",
            "key": "HKLM\\SOFTWARE\\Microsoft\\Cryptography\\Wintrust\\Config",
            "value_name": "EnableCertPaddingCheck",
            "value_type": "REG_DWORD",
            "value": 1,
            "label": "Enable Certificate Padding (64-bit) (EnableCertPaddingCheck=1)",
        },
        {
            "kind": "reg_set",
            "key": "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Cryptography\\Wintrust\\Config",
            "value_name": "EnableCertPaddingCheck",
            "value_type": "REG_DWORD",
            "value": 1,
            "label": "Enable Certificate Padding (32-bit subsystem) (EnableCertPaddingCheck=1)",
        },
    ]
