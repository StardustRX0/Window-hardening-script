from core.change_table_module import ChangeTableModule


class CIS_2_2_38(ChangeTableModule):
    cis_id = "2.2.38"
    title = 'Manage auditing and security log'
    profiles = ['dc']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeSecurityPrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544'],
            "label": 'Manage auditing and security log',
        }
    ]
