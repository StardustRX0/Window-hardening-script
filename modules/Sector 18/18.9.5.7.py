from core.change_table_module import ChangeTableModule


class CIS18_9_5_7(ChangeTableModule):
    """CIS 18.9.5.7"""

    cis_id = "18.9.5.7"
    title = "VBS: Secure Launch Configuration (Enabled)"
    description = 'Enables Secure Launch to protect the VBS environment from firmware-level exploits.'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": 'reg_set',
            "key": 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DeviceGuard',
            "value_name": 'ConfigureSystemGuardLaunch',
            "value_type": 'REG_DWORD',
            "value": 1,
            "label": 'Computer Configuration\\Policies\\Administrative Templates\\System\\Device Guard\\Turn On Virtualization Based Security: Secure Launch Configuration',
        },
    ]
