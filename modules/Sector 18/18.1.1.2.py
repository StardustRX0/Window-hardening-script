from core.change_table_module import ChangeTableModule


class CIS_18_1_1_2(ChangeTableModule):
    """18.1.1.2 Ensure 'Prevent enabling lock screen slide show'."""

    cis_id = "18.1.1.2"
    title = "Prevent enabling lock screen slide show"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "reg_set",
            "key": "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Personalization",
            "value_name": "NoLockScreenSlideshow",
            "value_type": "REG_DWORD",
            "value": 1,
            "label": "Prevent enabling lock screen slide show (NoLockScreenSlideshow=1)",
        },
    ]
