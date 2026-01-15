from core.change_table_module import ChangeTableModule


class CIS_2_2_3(ChangeTableModule):
    cis_id = "2.2.3"
    title = 'Access this computer from the network'
    profiles = ['ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeNetworkLogonRight',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544', '*S-1-5-11'],
            "label": 'Access this computer from the network',
        }
    ]
