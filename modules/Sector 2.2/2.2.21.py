from core.change_table_module import ChangeTableModule


class CIS_2_2_21(ChangeTableModule):
    cis_id = "2.2.21"
    title = 'Deny Network Access'
    profiles = ['dc']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeDenyNetworkLogonRight',
            "users_from": "users",
            "users_default": ['*S-1-5-32-546'],
            "label": 'Deny Network Access',
        }
    ]
