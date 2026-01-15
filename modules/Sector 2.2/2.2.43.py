from core.change_table_module import ChangeTableModule


class CIS_2_2_43(ChangeTableModule):
    cis_id = "2.2.43"
    title = 'Profile single process'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeProfileSingleProcessPrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544'],
            "label": 'Profile single process',
        }
    ]
