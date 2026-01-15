from core.change_table_module import ChangeTableModule


class CIS_2_2_36(ChangeTableModule):
    cis_id = "2.2.36"
    title = 'Lock Pages in Memory'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeLockMemoryPrivilege',
            "users_from": "users",
            "users_default": [],
            "label": 'Lock Pages in Memory',
        }
    ]
