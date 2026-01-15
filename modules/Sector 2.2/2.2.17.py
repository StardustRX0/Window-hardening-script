from core.change_table_module import ChangeTableModule


class CIS_2_2_17(ChangeTableModule):
    cis_id = "2.2.17"
    title = 'Shared Objects'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeCreatePermanentPrivilege',
            "users_from": "users",
            "users_default": [],
            "label": 'Shared Objects',
        }
    ]
