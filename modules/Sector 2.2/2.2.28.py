from core.change_table_module import ChangeTableModule


class CIS_2_2_28(ChangeTableModule):
    cis_id = "2.2.28"
    title = 'Enable delegation'
    profiles = ['dc']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeEnableDelegationPrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544'],
            "label": 'Enable delegation',
        }
    ]
