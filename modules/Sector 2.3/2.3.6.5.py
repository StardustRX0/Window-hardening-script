from core.change_table_module import ChangeTableModule


class CIS_2_3_6_5(ChangeTableModule):
    cis_id = "2.3.6.5"
    title = "Domain member: Maximum machine account password age"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            'kind': 'secedit_registry',
            'key': 'MACHINE\\System\\CurrentControlSet\\Services\\Netlogon\\Parameters\\MaximumPasswordAge',
            'value': '4,30',
            'label': 'MaximumPasswordAge = 30 days',
        },
    ]
