from core.change_table_module import ChangeTableModule


class CIS18_6_9_1(ChangeTableModule):
    """CIS 18.6.9.1 (L2)

    Ensure 'Turn on Mapper I/O (LLTDIO) driver' is set to 'Disabled'.
    """

    cis_id = "18.6.9.1"
    title = "Turn on Mapper I/O (LLTDIO) driver"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\LLTD",
            "value_name": "AllowLLTDIOOnDomain",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "LLTD: AllowLLTDIOOnDomain",
        },
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\LLTD",
            "value_name": "AllowLLTDIOOnPublicNet",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "LLTD: AllowLLTDIOOnPublicNet",
        },
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\LLTD",
            "value_name": "EnableLLTDIO",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "LLTD: EnableLLTDIO",
        },
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\LLTD",
            "value_name": "ProhibitLLTDIOOnPrivateNet",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "LLTD: ProhibitLLTDIOOnPrivateNet",
        },
    ]
