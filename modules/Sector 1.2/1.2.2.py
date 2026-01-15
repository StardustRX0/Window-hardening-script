from core.change_table_module import ChangeTableModule


class CIS_1_2_2(ChangeTableModule):
    cis_id = "1.2.2"
    title = 'Lockout Threshold'

    CHANGES = [
        {
            "kind": "secedit_system_access",
            "key": 'LockoutBadCount',
            "value_from": 'threshold',
            "default": 5,
            "label": 'Lockout Threshold',
        }
    ]
