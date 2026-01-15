from core.change_table_module import ChangeTableModule


class CIS_2_2_10(ChangeTableModule):
    cis_id = "2.2.10"
    title = 'Allow log on through Remote Desktop Services'
    profiles = ['ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeRemoteInteractiveLogonRight',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544', '*S-1-5-32-555'],
            "label": 'Allow log on through Remote Desktop Services',
        }
    ]
