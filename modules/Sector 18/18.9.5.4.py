from core.change_table_module import ChangeTableModule


class CIS18_9_5_4(ChangeTableModule):
    """CIS 18.9.5.4"""

    cis_id = "18.9.5.4"
    title = "VBS: Require UEFI Memory Attributes Table (True)"
    description = 'Requires the UEFI Memory Attributes Table before enabling VBS protection of Code Integrity, reducing risk of crashes on incompatible firmware.'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": 'reg_set',
            "key": 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DeviceGuard',
            "value_name": 'HVCIMATRequired',
            "value_type": 'REG_DWORD',
            "value": 1,
            "label": 'Computer Configuration\\Policies\\Administrative Templates\\System\\Device Guard\\Turn On Virtualization Based Security: Require UEFI Memory Attributes Table',
        },
    ]
