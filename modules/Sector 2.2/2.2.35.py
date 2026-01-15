from core.change_table_module import ChangeTableModule


class CIS_2_2_35(ChangeTableModule):
    cis_id = "2.2.35"
    title = 'Load and unload device drivers'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeLoadDriverPrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544'],
            "label": 'Load and unload device drivers',
        }
    ]
