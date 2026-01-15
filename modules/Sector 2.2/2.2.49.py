from core.change_table_module import ChangeTableModule


class CIS_2_2_49(ChangeTableModule):
    cis_id = "2.2.49"
    title = 'Take ownership of files or other objects'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeTakeOwnershipPrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544'],
            "label": 'Take ownership of files or other objects',
        }
    ]
