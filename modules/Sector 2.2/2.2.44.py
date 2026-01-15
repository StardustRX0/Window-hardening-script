from core.change_table_module import ChangeTableModule


class CIS_2_2_44(ChangeTableModule):
    cis_id = "2.2.44"
    title = 'Profile System Performance'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeSystemProfilePrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544', 'NT SERVICE\\WdiServiceHost'],
            "label": 'Profile System Performance',
        }
    ]
