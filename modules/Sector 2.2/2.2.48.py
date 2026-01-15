from core.change_table_module import ChangeTableModule


class CIS_2_2_48(ChangeTableModule):
    cis_id = "2.2.48"
    title = 'Sync Directory Data'
    profiles = ['dc']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeSyncAgentPrivilege',
            "users_from": "users",
            "users_default": [],
            "label": 'Sync Directory Data',
        }
    ]
