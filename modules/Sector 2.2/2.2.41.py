from core.change_table_module import ChangeTableModule


class CIS_2_2_41(ChangeTableModule):
    cis_id = "2.2.41"
    title = 'Modify firmware environment values'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeSystemEnvironmentPrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544'],
            "label": 'Modify firmware environment values',
        }
    ]
