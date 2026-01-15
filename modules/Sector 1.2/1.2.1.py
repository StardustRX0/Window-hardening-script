from core.change_table_module import ChangeTableModule


class CIS_1_2_1(ChangeTableModule):
    cis_id = "1.2.1"
    title = 'Lockout Duration'

    CHANGES = [
        {
            "kind": "secedit_system_access",
            "key": 'LockoutDuration',
            "value_from": 'duration',
            "default": 15,
            "label": 'Lockout Duration',
        }
    ]
