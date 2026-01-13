from core.change_table_module import ChangeTableModule


class CIS18_9_5_5(ChangeTableModule):
    """CIS 18.9.5.5"""

    cis_id = "18.9.5.5"
    title = "VBS: Credential Guard Configuration (Enabled with UEFI lock) (MS only)"
    description = 'Enables Windows Defender Credential Guard with UEFI lock on Member Servers (not Domain Controllers).'
    profiles = ['ms']

    CHANGES = [
        {
            "kind": 'reg_set',
            "key": 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DeviceGuard',
            "value_name": 'LsaCfgFlags',
            "value_type": 'REG_DWORD',
            "value": 1,
            "label": 'Computer Configuration\\Policies\\Administrative Templates\\System\\Device Guard\\Turn On Virtualization Based Security: Credential Guard Configuration',
        },
    ]
