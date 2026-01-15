from core.change_table_module import ChangeTableModule


class CIS_2_2_40(ChangeTableModule):
    cis_id = "2.2.40"
    title = 'Modify an object label'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeRelabelPrivilege',
            "users_from": "users",
            "users_default": [],
            "label": 'Modify an object label',
        }
    ]
