from core.change_table_module import ChangeTableModule


class CIS18_9_19_3(ChangeTableModule):
    """CIS 18.9.19.3"""

    cis_id = "18.9.19.3"
    title = "Configure registry policy processing: Process even if GPOs have not changed (TRUE)"
    description = 'Forces registry policies to reapply even when unchanged, helping revert unauthorized local changes.'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": 'reg_set',
            "key": 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Group Policy\\{35378EAC-683F-11D2-A89A-00C04FBBCFA2}',
            "value_name": 'NoGPOListChanges',
            "value_type": 'REG_DWORD',
            "value": 0,
            "label": 'Computer Configuration\\Policies\\Administrative Templates\\System\\Group Policy\\Configure registry policy processing: Process even if the Group Policy objects have not changed',
        },
    ]
