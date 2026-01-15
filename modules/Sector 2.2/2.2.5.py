from core.change_table_module import ChangeTableModule


class CIS_2_2_5(ChangeTableModule):
    cis_id = "2.2.5"
    title = 'Add Workstations'
    profiles = ['dc']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeMachineAccountPrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544'],
            "label": 'Add Workstations',
        }
    ]
