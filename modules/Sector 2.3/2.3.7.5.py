from core.change_table_module import ChangeTableModule


class CIS_2_3_7_5(ChangeTableModule):
    cis_id = "2.3.7.5"
    title = "Interactive logon: Message title for users attempting to log on"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            'kind': 'secedit_registry',
            'key': 'MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\LegalNoticeCaption',
            'value_from': 'caption',
            'value_template': '1,"{value}"',
            'label': 'LegalNoticeCaption',
        },
    ]
