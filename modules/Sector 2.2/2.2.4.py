from core.change_table_module import ChangeTableModule


class CIS_2_2_4(ChangeTableModule):
    cis_id = "2.2.4"
    title = 'Act as OS'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeTcbPrivilege',
            "users_from": "users",
            "users_default": [],
            "label": 'Act as OS',
        }
    ]
