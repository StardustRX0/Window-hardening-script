from core.change_table_module import ChangeTableModule


class CIS_2_3_9_3(ChangeTableModule):
    cis_id = "2.3.9.3"
    title = "Microsoft network server: Digitally sign communications (if client agrees)"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            'kind': 'secedit_registry',
            'key': 'MACHINE\\System\\CurrentControlSet\\Services\\LanmanServer\\Parameters\\EnableSecuritySignature',
            'value': '4,1',
            'label': 'EnableSecuritySignature = 1 (Enabled)',
        },
    ]
