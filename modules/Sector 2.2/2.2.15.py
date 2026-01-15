from core.change_table_module import ChangeTableModule


class CIS_2_2_15(ChangeTableModule):
    cis_id = "2.2.15"
    title = 'Create Token Object'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeCreateTokenPrivilege',
            "users_from": "users",
            "users_default": [],
            "label": 'Create Token Object',
        }
    ]
