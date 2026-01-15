from core.change_table_module import ChangeTableModule


class CIS_1_1_4(ChangeTableModule):
    cis_id = "1.1.4"
    title = 'Min Length'

    CHANGES = [
        {
            "kind": "secedit_system_access",
            "key": 'MinimumPasswordLength',
            "value_from": 'min_length',
            "default": 14,
            "label": 'Min Length',
        }
    ]
