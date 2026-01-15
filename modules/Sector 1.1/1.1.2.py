from core.change_table_module import ChangeTableModule


class CIS_1_1_2(ChangeTableModule):
    cis_id = "1.1.2"
    title = 'Max Age'

    CHANGES = [
        {
            "kind": "secedit_system_access",
            "key": 'MaximumPasswordAge',
            "value_from": 'max_age',
            "default": 365,
            "label": 'Max Age',
        }
    ]
