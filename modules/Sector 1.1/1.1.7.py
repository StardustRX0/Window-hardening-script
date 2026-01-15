from core.change_table_module import ChangeTableModule


class CIS_1_1_7(ChangeTableModule):
    cis_id = "1.1.7"
    title = 'Reversible Enc'

    CHANGES = [
        {
            "kind": "secedit_system_access",
            "key": 'ClearTextPassword',
            "value_from": 'reversible',
            "default": 0,
            "label": 'Reversible Enc',
        }
    ]
