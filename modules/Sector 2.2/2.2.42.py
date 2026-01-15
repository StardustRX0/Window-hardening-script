from core.change_table_module import ChangeTableModule


class CIS_2_2_42(ChangeTableModule):
    cis_id = "2.2.42"
    title = 'Perform volume maintenance tasks'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeManageVolumePrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544'],
            "label": 'Perform volume maintenance tasks',
        }
    ]
