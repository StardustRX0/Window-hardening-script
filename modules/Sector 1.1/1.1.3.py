from core.change_table_module import ChangeTableModule


class CIS_1_1_3(ChangeTableModule):
    cis_id = "1.1.3"
    title = 'Min Age'

    CHANGES = [
        {
            "kind": "secedit_system_access",
            "key": 'MinimumPasswordAge',
            "value_from": 'min_age',
            "default": 1,
            "label": 'Min Age',
        }
    ]
