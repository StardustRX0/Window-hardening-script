from core.change_table_module import ChangeTableModule


class CIS_2_3_6_4(ChangeTableModule):
    cis_id = "2.3.6.4"
    title = "Domain member: Disable machine account password changes"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            'kind': 'secedit_registry',
            'key': 'MACHINE\\System\\CurrentControlSet\\Services\\Netlogon\\Parameters\\DisablePasswordChange',
            'value': '4,0',
            'label': 'DisablePasswordChange = 0 (allow password changes)',
        },
    ]
