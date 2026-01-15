from core.change_table_module import ChangeTableModule


class CIS_2_2_19(ChangeTableModule):
    cis_id = "2.2.19"
    title = 'Create symbolic links'
    profiles = ['ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeCreateSymbolicLinkPrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544', 'NT VIRTUAL MACHINE\\\\Virtual Machines'],
            "label": 'Create symbolic links',
        }
    ]
