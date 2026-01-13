from core.change_table_module import ChangeTableModule


class CIS_2_3_8_3(ChangeTableModule):
    cis_id = "2.3.8.3"
    title = "Microsoft network client: Send unencrypted password to third-party SMB servers"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            'kind': 'secedit_registry',
            'key': 'MACHINE\\System\\CurrentControlSet\\Services\\LanmanWorkstation\\Parameters\\EnablePlainTextPassword',
            'value': '4,0',
            'label': 'EnablePlainTextPassword = 0 (Disabled)',
        },
    ]
