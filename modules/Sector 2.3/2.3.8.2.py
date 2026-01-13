from core.change_table_module import ChangeTableModule


class CIS_2_3_8_2(ChangeTableModule):
    cis_id = "2.3.8.2"
    title = "Microsoft network client: Digitally sign communications (if server agrees)"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            'kind': 'secedit_registry',
            'key': 'MACHINE\\System\\CurrentControlSet\\Services\\LanmanWorkstation\\Parameters\\EnableSecuritySignature',
            'value': '4,1',
            'label': 'EnableSecuritySignature = 1 (Enabled)',
        },
    ]
