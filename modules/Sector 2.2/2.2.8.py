from core.change_table_module import ChangeTableModule


class CIS_2_2_8(ChangeTableModule):
    cis_id = "2.2.8"
    title = 'Allow log on locally'
    profiles = ['ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeInteractiveLogonRight',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544'],
            "label": 'Allow log on locally',
        }
    ]
