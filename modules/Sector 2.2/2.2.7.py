from core.change_table_module import ChangeTableModule


class CIS_2_2_7(ChangeTableModule):
    cis_id = "2.2.7"
    title = 'Allow Log on Locally'
    profiles = ['dc']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeInteractiveLogonRight',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544', '*S-1-5-9'],
            "label": 'Allow Log on Locally',
        }
    ]
