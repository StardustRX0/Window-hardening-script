from core.change_table_module import ChangeTableModule


class CIS_2_2_9(ChangeTableModule):
    cis_id = "2.2.9"
    title = 'Remote Desktop Log on'
    profiles = ['dc']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeRemoteInteractiveLogonRight',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544'],
            "label": 'Remote Desktop Log on',
        }
    ]
