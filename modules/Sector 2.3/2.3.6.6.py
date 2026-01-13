from core.change_table_module import ChangeTableModule


class CIS_2_3_6_6(ChangeTableModule):
    cis_id = "2.3.6.6"
    title = "Domain member: Require strong (Windows 2000 or later) session key"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            'kind': 'secedit_registry',
            'key': 'MACHINE\\System\\CurrentControlSet\\Services\\Netlogon\\Parameters\\RequireStrongKey',
            'value': '4,1',
            'label': 'RequireStrongKey = 1 (require strong session key)',
        },
    ]
