from core.change_table_module import ChangeTableModule


class CIS18_9_5_3(ChangeTableModule):
    """CIS 18.9.5.3"""

    cis_id = "18.9.5.3"
    title = "VBS: Virtualization Based Protection of Code Integrity (Enabled with UEFI lock)"
    description = 'Enables virtualization-based protection of Kernel Mode Code Integrity, with UEFI lock so it cannot be disabled remotely.'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": 'reg_set',
            "key": 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DeviceGuard',
            "value_name": 'HypervisorEnforcedCodeIntegrity',
            "value_type": 'REG_DWORD',
            "value": 1,
            "label": 'Computer Configuration\\Policies\\Administrative Templates\\System\\Device Guard\\Turn On Virtualization Based Security: Virtualization Based Protection of Code Integrity',
        },
    ]
