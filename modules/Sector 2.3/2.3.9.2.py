from core.change_table_module import ChangeTableModule


class CIS_2_3_9_2(ChangeTableModule):
    cis_id = "2.3.9.2"
    title = "Microsoft network server: Digitally sign communications (always)"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            'kind': 'secedit_registry',
            'key': 'MACHINE\\System\\CurrentControlSet\\Services\\LanmanServer\\Parameters\\RequireSecuritySignature',
            'value': '4,1',
            'label': 'RequireSecuritySignature = 1 (Enabled)',
        },
    ]
