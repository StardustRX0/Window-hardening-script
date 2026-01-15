from core.change_table_module import ChangeTableModule


class CIS_2_2_12(ChangeTableModule):
    cis_id = "2.2.12"
    title = 'System Time'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeSystemtimePrivilege',
            "users_from": "users",
            "users_default": [],
            "label": 'System Time',
        }
    ]
