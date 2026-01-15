from core.change_table_module import ChangeTableModule


class CIS_2_2_30(ChangeTableModule):
    cis_id = "2.2.30"
    title = 'Shut down the system'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeRemoteShutdownPrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544'],
            "label": 'Shut down the system',
        }
    ]
