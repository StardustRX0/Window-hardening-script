from core.change_table_module import ChangeTableModule


class CIS_18_1_1_1(ChangeTableModule):
    """18.1.1.1 (L1) Ensure 'Prevent enabling lock screen camera' is set to 'Enabled'."""

    cis_id = "18.1.1.1"
    title = "Ensure 'Prevent enabling lock screen camera' is set to 'Enabled'"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\Personalization",
            "value_name": "NoLockScreenCamera",
            "value_type": "REG_DWORD",
            "value": 1,
            "label": "Prevent enabling lock screen camera (NoLockScreenCamera=1)",
        }
    ]
