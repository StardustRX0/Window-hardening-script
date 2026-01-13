from core.change_table_module import ChangeTableModule


class CIS_2_3_7_3(ChangeTableModule):
    cis_id = "2.3.7.3"
    title = "Interactive logon: Machine inactivity limit"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            'kind': 'secedit_registry',
            'key': 'MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\InactivityTimeoutSecs',
            'value': '4,900',
            'label': 'InactivityTimeoutSecs = 900 seconds',
        },
    ]
