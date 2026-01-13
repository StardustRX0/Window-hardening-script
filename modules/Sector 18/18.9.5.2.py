from core.change_table_module import ChangeTableModule


class CIS18_9_5_2(ChangeTableModule):
    """CIS 18.9.5.2"""

    cis_id = "18.9.5.2"
    title = "VBS Platform Security Level (Secure Boot or higher)"
    description = "Sets VBS Platform Security Level to 'Secure Boot' (1). CIS allows 1 (Secure Boot) or 3 (Secure Boot and DMA Protection). This baseline uses 1 by default."
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": 'reg_set',
            "key": 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DeviceGuard',
            "value_name": 'RequirePlatformSecurityFeatures',
            "value_type": 'REG_DWORD',
            "value": 1,
            "label": 'Computer Configuration\\Policies\\Administrative Templates\\System\\Device Guard\\Turn On Virtualization Based Security: Select Platform Security Level',
        },
    ]
