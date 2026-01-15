from core.change_table_module import ChangeTableModule


class CIS_2_2_29(ChangeTableModule):
    cis_id = "2.2.29"
    title = 'Enable computer and user accounts to be trusted for delegation'
    profiles = ['ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeEnableDelegationPrivilege',
            "users_from": "users",
            "users_default": [],
            "label": 'Enable computer and user accounts to be trusted for delegation',
        }
    ]
