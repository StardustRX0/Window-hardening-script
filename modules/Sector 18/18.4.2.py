from core.change_table_module import ChangeTableModule


class CIS_18_4_2(ChangeTableModule):
    """18.4.2 Ensure 'Configure SMB v1 client driver (Disable driver)'."""

    cis_id = "18.4.2"
    title = "Configure SMB v1 client driver (Disable driver)"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "reg_set",
            "key": "HKLM\\SYSTEM\\CurrentControlSet\\Services\\mrxsmb10",
            "value_name": "Start",
            "value_type": "REG_DWORD",
            "value": 4,
            "label": "Disable SMBv1 client driver (mrxsmb10 Start=4)",
        },
    ]
