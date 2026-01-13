from core.change_table_module import ChangeTableModule


class CIS_18_1_3(ChangeTableModule):
    """18.1.3 Ensure 'Allow Online Tips'."""

    cis_id = "18.1.3"
    title = "Allow Online Tips"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "reg_set",
            "key": "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
            "value_name": "AllowOnlineTips",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "Disable Allow Online Tips (AllowOnlineTips=0)",
        },
    ]
