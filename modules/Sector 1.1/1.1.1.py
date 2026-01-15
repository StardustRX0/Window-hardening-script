from core.change_table_module import ChangeTableModule


class CIS_1_1_1(ChangeTableModule):
    cis_id = "1.1.1"
    title = 'Pass History'

    CHANGES = [
        {
            "kind": "secedit_system_access",
            "key": 'PasswordHistorySize',
            "value_from": 'history_count',
            "default": 24,
            "label": 'Pass History',
        }
    ]
