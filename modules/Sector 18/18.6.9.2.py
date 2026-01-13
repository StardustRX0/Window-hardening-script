from core.change_table_module import ChangeTableModule


class CIS18_6_9_2(ChangeTableModule):
    """CIS 18.6.9.2 (L2)

    Ensure 'Turn on Responder (RSPNDR) driver' is set to 'Disabled'.
    """

    cis_id = "18.6.9.2"
    title = "Turn on Responder (RSPNDR) driver"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\LLTD",
            "value_name": "AllowRspndrOnDomain",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "LLTD: AllowRspndrOnDomain",
        },
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\LLTD",
            "value_name": "AllowRspndrOnPublicNet",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "LLTD: AllowRspndrOnPublicNet",
        },
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\LLTD",
            "value_name": "EnableRspndr",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "LLTD: EnableRspndr",
        },
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\LLTD",
            "value_name": "ProhibitRspndrOnPrivateNet",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "LLTD: ProhibitRspndrOnPrivateNet",
        },
    ]
