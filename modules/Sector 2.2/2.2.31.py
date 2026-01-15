from core.change_table_module import ChangeTableModule


class CIS_2_2_31(ChangeTableModule):
    cis_id = "2.2.31"
    title = 'Generate security audits'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "user_right",
            "right": 'SeAuditPrivilege',
            "users_from": "users",
            "users_default": ['*S-1-5-19', '*S-1-5-20'],
            "label": 'Generate security audits',
        }
    ]
