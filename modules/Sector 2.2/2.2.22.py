from core.change_table_module import ChangeTableModule


class CIS_2_2_22(ChangeTableModule):
    cis_id = "2.2.22"
    title = 'Deny access to this computer from the network'
    profiles = ['ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeDenyNetworkLogonRight',
            "users_from": "users",
            "users_default": ['*S-1-5-32-546', '*S-1-5-114'],
            "label": 'Deny access to this computer from the network',
        }
    ]
