from core.change_table_module import ChangeTableModule


class CIS_2_2_47(ChangeTableModule):
    cis_id = "2.2.47"
    title = 'Shut down the system'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeShutdownPrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544'],
            "label": 'Shut down the system',
        }
    ]
