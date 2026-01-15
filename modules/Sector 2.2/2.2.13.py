from core.change_table_module import ChangeTableModule


class CIS_2_2_13(ChangeTableModule):
    cis_id = "2.2.13"
    title = 'Time Zone'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeTimeZonePrivilege',
            "users_from": "users",
            "users_default": [],
            "label": 'Time Zone',
        }
    ]
