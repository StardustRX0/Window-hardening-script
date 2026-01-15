from core.change_table_module import ChangeTableModule


class CIS_2_2_24(ChangeTableModule):
    cis_id = "2.2.24"
    title = 'Deny Service Logon'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeDenyServiceLogonRight',
            "users_from": "users",
            "users_default": ['*S-1-5-32-546'],
            "label": 'Deny Service Logon',
        }
    ]
