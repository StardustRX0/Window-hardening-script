from core.change_table_module import ChangeTableModule


class CIS_2_3_6_3(ChangeTableModule):
    cis_id = "2.3.6.3"
    title = "Domain member: Digitally sign secure channel data (when possible)"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            'kind': 'secedit_registry',
            'key': 'MACHINE\\System\\CurrentControlSet\\Services\\Netlogon\\Parameters\\SignSecureChannel',
            'value': '4,1',
            'label': 'Enable SignSecureChannel (sign secure channel when possible)',
        },
    ]
