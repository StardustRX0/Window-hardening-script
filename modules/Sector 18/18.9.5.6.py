from core.change_table_module import ChangeTableModule


class CIS18_9_5_6(ChangeTableModule):
    """CIS 18.9.5.6"""

    cis_id = "18.9.5.6"
    title = "VBS: Credential Guard Configuration (Disabled) (DC only)"
    description = 'Disables Credential Guard on Domain Controllers (unsupported and can cause crashes).'
    profiles = ['dc']

    CHANGES = [
        {
            "kind": 'reg_set',
            "key": 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DeviceGuard',
            "value_name": 'LsaCfgFlags',
            "value_type": 'REG_DWORD',
            "value": 0,
            "label": 'Computer Configuration\\Policies\\Administrative Templates\\System\\Device Guard\\Turn On Virtualization Based Security: Credential Guard Configuration',
        },
    ]
