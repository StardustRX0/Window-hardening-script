from core.change_table_module import ChangeTableModule


class CIS18_9_13_1(ChangeTableModule):
    """CIS 18.9.13.1"""

    cis_id = "18.9.13.1"
    title = "Boot-Start Driver Initialization Policy (Good, unknown and bad but critical)"
    description = 'Controls which boot-start drivers are allowed. Recommended setting blocks known bad drivers except those needed for boot.'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": 'reg_set',
            "key": 'HKLM\\SYSTEM\\CurrentControlSet\\Policies\\EarlyLaunch',
            "value_name": 'DriverLoadPolicy',
            "value_type": 'REG_DWORD',
            "value": 3,
            "label": 'Computer Configuration\\Policies\\Administrative Templates\\System\\Early Launch Antimalware\\Boot-Start Driver Initialization Policy',
        },
    ]
