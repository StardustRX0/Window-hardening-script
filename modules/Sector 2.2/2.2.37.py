from core.change_table_module import ChangeTableModule


class CIS_2_2_37(ChangeTableModule):
    cis_id = "2.2.37"
    title = 'Log on as a batch job'
    profiles = ['dc']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeBatchLogonRight',
            "users_from": "users",
            "users_default": ['*S-1-5-32-544'],
            "label": 'Log on as a batch job',
        }
    ]
