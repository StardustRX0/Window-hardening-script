from core.change_table_module import ChangeTableModule


class CIS_1_2_4(ChangeTableModule):
    cis_id = "1.2.4"
    title = 'Reset Lockout'

    CHANGES = [
        {
            "kind": "secedit_system_access",
            "key": 'ResetLockoutCount',
            "value_from": 'reset_after',
            "default": 15,
            "label": 'Reset Lockout',
        }
    ]
