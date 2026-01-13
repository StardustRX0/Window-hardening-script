from core.change_table_module import ChangeTableModule


class CIS_18_1_2_2(ChangeTableModule):
    """18.1.2.2 Ensure 'Allow users to enable online speech recognition services'."""

    cis_id = "18.1.2.2"
    title = "Allow users to enable online speech recognition services"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "reg_set",
            "key": "HKLM\\SOFTWARE\\Policies\\Microsoft\\InputPersonalization",
            "value_name": "AllowInputPersonalization",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "Disable online speech recognition services (AllowInputPersonalization=0)",
        },
    ]
