from core.change_table_module import ChangeTableModule


class CIS18_6_7_1(ChangeTableModule):
    """CIS 18.6.7.1 (L1)

    Ensure 'Mandate the minimum version of SMB' is set to 'Enabled: 3.1.1'.
    """

    id = "18.6.7.1"
    title = "Mandate the minimum version of SMB"
    profiles = ["dc", "ms"]

    # 785 (decimal) = 0x311, representing SMB 3.1.1
    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\LanmanServer",
            "value_name": "MinSmb2Dialect",
            "value_type": "REG_DWORD",
            "value": 785,
            "label": "Min SMB dialect (MinSmb2Dialect=785 / 0x311)",
        }
    ]
