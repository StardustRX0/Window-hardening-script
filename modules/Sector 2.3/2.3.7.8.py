from core.change_table_module import ChangeTableModule


class CIS_2_3_7_8(ChangeTableModule):
    cis_id = "2.3.7.8"
    title = "Interactive logon: Require Domain Controller Authentication to unlock workstation"
    # CIS: Member Server only
    profiles = ['ms']

    CHANGES = [
        {
            'kind': 'secedit_registry',
            'key': 'MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\ForceUnlockLogon',
            'value': '4,1',
            'label': 'ForceUnlockLogon = 1 (Enabled)',
        },
    ]
