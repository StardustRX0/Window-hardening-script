from core.change_table_module import ChangeTableModule


class CIS_2_3_7_4(ChangeTableModule):
    cis_id = "2.3.7.4"
    title = "Interactive logon: Message text for users attempting to log on"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            'kind': 'secedit_registry',
            'key': 'MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\LegalNoticeText',
            'value_from': 'text',
            'value_template': '1,"{value}"',
            'label': 'LegalNoticeText',
        },
    ]
