from core.change_table_module import ChangeTableModule


class CIS_1_1_5(ChangeTableModule):
    cis_id = "1.1.5"
    title = 'Complexity'

    CHANGES = [
        {
            "kind": "secedit_system_access",
            "key": 'PasswordComplexity',
            "value_from": 'complexity',
            "default": 1,
            "label": 'Complexity',
        }
    ]
