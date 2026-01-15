from core.change_table_module import ChangeTableModule


class CIS_2_2_46(ChangeTableModule):
    cis_id = "2.2.46"
    title = 'Restore files and directories'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeRestorePrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544'],
            "label": 'Restore files and directories',
        }
    ]
