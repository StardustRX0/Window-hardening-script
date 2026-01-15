from core.change_table_module import ChangeTableModule


class CIS_2_2_33(ChangeTableModule):
    cis_id = "2.2.33"
    title = 'Impersonate a client after authentication'
    profiles = ['ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeImpersonatePrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544', '*S-1-5-19', '*S-1-5-20', '*S-1-5-6'],
            "label": 'Impersonate a client after authentication',
        }
    ]
