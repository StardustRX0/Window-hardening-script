from core.change_table_module import ChangeTableModule


class CIS_2_2_2(ChangeTableModule):
    cis_id = "2.2.2"
    title = 'Network Access'
    profiles = ['dc']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeNetworkLogonRight',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544', '*S-1-5-11', '*S-1-5-9'],
            "label": 'Network Access',
        }
    ]
