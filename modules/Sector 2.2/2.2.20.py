from core.change_table_module import ChangeTableModule


class CIS_2_2_20(ChangeTableModule):
    cis_id = "2.2.20"
    title = 'Debug Programs'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeDebugPrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544'],
            "label": 'Debug Programs',
        }
    ]
