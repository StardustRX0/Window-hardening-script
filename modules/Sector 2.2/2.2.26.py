from core.change_table_module import ChangeTableModule


class CIS_2_2_26(ChangeTableModule):
    cis_id = "2.2.26"
    title = 'Deny Remote Interactive Logon'
    profiles = ['dc']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeDenyRemoteInteractiveLogonRight',
            "users_from": "users",
            "users_default": ['*S-1-5-32-546'],
            "label": 'Deny Remote Interactive Logon',
        }
    ]
