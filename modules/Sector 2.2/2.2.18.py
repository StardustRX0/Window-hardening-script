from core.change_table_module import ChangeTableModule


class CIS_2_2_18(ChangeTableModule):
    cis_id = "2.2.18"
    title = 'Create symbolic links'
    profiles = ['dc']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeCreateSymbolicLinkPrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544'],
            "label": 'Create symbolic links',
        }
    ]
