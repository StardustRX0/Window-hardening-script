from core.change_table_module import ChangeTableModule


class CIS_2_2_6(ChangeTableModule):
    cis_id = "2.2.6"
    title = 'Memory Quotas'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeIncreaseQuotaPrivilege',
            "users_from": "users",
            "users_default": [],
            "label": 'Memory Quotas',
        }
    ]
