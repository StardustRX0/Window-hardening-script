from core.change_table_module import ChangeTableModule


class CIS_2_2_16(ChangeTableModule):
    cis_id = "2.2.16"
    title = 'Create Global Objects'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeCreateGlobalPrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544', '*S-1-5-19', '*S-1-5-20', '*S-1-5-6'],
            "label": 'Create Global Objects',
        }
    ]
