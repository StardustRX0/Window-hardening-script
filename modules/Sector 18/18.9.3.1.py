from core.change_table_module import ChangeTableModule


class CIS18_9_3_1(ChangeTableModule):
    """CIS 18.9.3.1"""

    cis_id = "18.9.3.1"
    title = "Include command line in process creation events"
    description = 'Includes full command line details in process creation audit events. This improves investigation and threat hunting by showing what arguments were used.'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": 'reg_set',
            "key": 'HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\Audit',
            "value_name": 'ProcessCreationIncludeCmdLine_Enabled',
            "value_type": 'REG_DWORD',
            "value": 1,
            "label": 'Computer Configuration\\Policies\\Administrative Templates\\System\\Audit Process Creation: Include command line in process creation events',
        },
    ]
