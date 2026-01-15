from core.change_table_module import ChangeTableModule


class CIS_2_2_14(ChangeTableModule):
    cis_id = "2.2.14"
    title = 'Create a pagefile'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeCreatePagefilePrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544'],
            "label": 'Create a pagefile',
        }
    ]
