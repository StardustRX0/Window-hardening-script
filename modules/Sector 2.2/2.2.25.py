from core.change_table_module import ChangeTableModule


class CIS_2_2_25(ChangeTableModule):
    cis_id = "2.2.25"
    title = 'Deny Interactive Logon'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeDenyInteractiveLogonRight',
            "users_from": "users",
            "users_default": ['*S-1-5-32-546'],
            "label": 'Deny Interactive Logon',
        }
    ]
