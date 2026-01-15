from core.change_table_module import ChangeTableModule


class CIS_2_2_27(ChangeTableModule):
    cis_id = "2.2.27"
    title = 'Deny log on through Remote Desktop Services'
    profiles = ['ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeDenyRemoteInteractiveLogonRight',
            "users_from": "users",
            "users_default": ['*S-1-5-32-546', '*S-1-5-113'],
            "label": 'Deny log on through Remote Desktop Services',
        }
    ]
