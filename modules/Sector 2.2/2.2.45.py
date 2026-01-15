from core.change_table_module import ChangeTableModule


class CIS_2_2_45(ChangeTableModule):
    cis_id = "2.2.45"
    title = 'Replace a process level token'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeAssignPrimaryTokenPrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-19', '*S-1-5-20'],
            "label": 'Replace a process level token',
        }
    ]
