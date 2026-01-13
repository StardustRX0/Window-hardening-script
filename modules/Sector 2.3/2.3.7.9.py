from core.change_table_module import ChangeTableModule


class CIS_2_3_7_9(ChangeTableModule):
    cis_id = "2.3.7.9"
    title = "Interactive logon: Smart card removal behavior"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            'kind': 'secedit_registry',
            'key': 'MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\ScRemoveOption',
            # CIS: 'Lock Workstation' or higher. Values are stored as REG_SZ:
            #   1 = Lock Workstation
            #   2 = Force Logoff
            #   3 = Disconnect if a Remote Desktop Services session
            'value': '1,"1"',
            'label': 'ScRemoveOption = 1 (Lock Workstation)',
        },
    ]
