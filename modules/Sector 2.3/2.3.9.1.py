from core.change_table_module import ChangeTableModule


class CIS_2_3_9_1(ChangeTableModule):
    cis_id = "2.3.9.1"
    title = "Microsoft network server: Amount of idle time required before suspending session"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            'kind': 'secedit_registry',
            'key': 'MACHINE\\System\\CurrentControlSet\\Services\\LanmanServer\\Parameters\\AutoDisconnect',
            # CIS: 15 or fewer, but not 0. Default is 15.
            'value': '4,15',
            'label': 'AutoDisconnect = 15 (minutes)',
        },
    ]
