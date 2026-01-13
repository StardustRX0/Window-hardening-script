from core.change_table_module import ChangeTableModule


class CIS_2_3_7_1(ChangeTableModule):
    cis_id = "2.3.7.1"
    title = "Interactive logon: Do not require CTRL+ALT+DEL"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            'kind': 'secedit_registry',
            'key': 'MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\DisableCAD',
            'value': '4,0',
            'label': 'DisableCAD = 0 (require CTRL+ALT+DEL)',
        },
    ]
