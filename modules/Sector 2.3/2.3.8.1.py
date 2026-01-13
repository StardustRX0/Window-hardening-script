from core.change_table_module import ChangeTableModule


class CIS_2_3_8_1(ChangeTableModule):
    cis_id = "2.3.8.1"
    title = "Microsoft network client: Digitally sign communications (always)"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            'kind': 'secedit_registry',
            'key': 'MACHINE\\System\\CurrentControlSet\\Services\\LanmanWorkstation\\Parameters\\RequireSecuritySignature',
            'value': '4,1',
            'label': 'RequireSecuritySignature = 1 (Enabled)',
        },
    ]
