from core.change_table_module import ChangeTableModule


class CIS_2_3_7_2(ChangeTableModule):
    cis_id = "2.3.7.2"
    title = "Interactive logon: Don't display last signed-in"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            'kind': 'secedit_registry',
            'key': 'MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\DontDisplayLastUserName',
            'value': '4,1',
            'label': 'DontDisplayLastUserName = 1',
        },
    ]
