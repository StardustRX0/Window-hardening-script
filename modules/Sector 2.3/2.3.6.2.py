from core.change_table_module import ChangeTableModule


class CIS_2_3_6_2(ChangeTableModule):
    cis_id = "2.3.6.2"
    title = "Domain member: Digitally encrypt secure channel data (when possible)"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            'kind': 'secedit_registry',
            'key': 'MACHINE\\System\\CurrentControlSet\\Services\\Netlogon\\Parameters\\SealSecureChannel',
            'value': '4,1',
            'label': 'Enable SealSecureChannel (encrypt secure channel when possible)',
        },
    ]
