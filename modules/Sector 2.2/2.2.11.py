from core.change_table_module import ChangeTableModule


class CIS_2_2_11(ChangeTableModule):
    cis_id = "2.2.11"
    title = 'Back up files and directories'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeBackupPrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544'],
            "label": 'Back up files and directories',
        }
    ]
