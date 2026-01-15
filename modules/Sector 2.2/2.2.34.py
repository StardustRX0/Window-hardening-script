from core.change_table_module import ChangeTableModule


class CIS_2_2_34(ChangeTableModule):
    cis_id = "2.2.34"
    title = 'Increase scheduling priority'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeIncreaseBasePriorityPrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544', 'Window Manager\\Window Manager Group'],
            "label": 'Increase scheduling priority',
        }
    ]
