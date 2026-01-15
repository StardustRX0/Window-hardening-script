from core.change_table_module import ChangeTableModule


class CIS_2_2_23(ChangeTableModule):
    cis_id = "2.2.23"
    title = 'Deny Batch Access'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeDenyBatchLogonRight',
            "users_from": "users",
            "users_default": ['*S-1-5-32-546'],
            "label": 'Deny Batch Access',
        }
    ]
