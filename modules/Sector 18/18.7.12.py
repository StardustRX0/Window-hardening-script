from core.change_table_module import ChangeTableModule


class CIS18_7_12(ChangeTableModule):
    """CIS 18.7.12"""

    cis_id = "18.7.12"
    title = "Point and Print: warn and prompt for elevation on driver updates"
    description = 'Shows warning and elevation prompt when updating drivers for an existing Point and Print connection. This helps prevent silent driver updates that could introduce malicious code.'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": 'reg_set',
            "key": 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\Printers\\PointAndPrint',
            "value_name": 'UpdatePromptSettings',
            "value_type": 'REG_DWORD',
            "value": 0,
            "label": 'Computer Configuration\\Policies\\Administrative Templates\\Printers\\Point and Print Restrictions: When updating drivers for an existing connection',
        },
    ]
