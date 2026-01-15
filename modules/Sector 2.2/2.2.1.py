from core.change_table_module import ChangeTableModule


class CIS_2_2_1(ChangeTableModule):
    cis_id = "2.2.1"
    title = 'Cred Man Access'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeTrustedCredManAccessPrivilege',
            "users_from": "users",
            "users_default": [],
            "label": 'Cred Man Access',
        }
    ]
