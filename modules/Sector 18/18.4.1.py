from core.change_table_module import ChangeTableModule


class CIS_18_4_1(ChangeTableModule):
    """18.4.1 Ensure 'Apply UAC restrictions to local accounts on network logons'."""

    cis_id = "18.4.1"
    title = "Apply UAC restrictions to local accounts on network logons"
    profiles = ['ms']

    CHANGES = [
        {
            "kind": "reg_set",
            "key": "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
            "value_name": "LocalAccountTokenFilterPolicy",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "Apply UAC restrictions to local accounts on network logons (LocalAccountTokenFilterPolicy=0)",
        },
    ]
