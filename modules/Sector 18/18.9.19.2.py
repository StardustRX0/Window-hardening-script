from core.change_table_module import ChangeTableModule


class CIS18_9_19_2(ChangeTableModule):
    """CIS 18.9.19.2"""

    cis_id = "18.9.19.2"
    title = "Configure registry policy processing: Do not apply during periodic background processing (FALSE)"
    description = "Ensures registry-based Group Policy settings refresh in the background by keeping 'Do not apply during periodic background processing' unchecked."
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": 'reg_set',
            "key": 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Group Policy\\{35378EAC-683F-11D2-A89A-00C04FBBCFA2}',
            "value_name": 'NoBackgroundPolicy',
            "value_type": 'REG_DWORD',
            "value": 0,
            "label": 'Computer Configuration\\Policies\\Administrative Templates\\System\\Group Policy\\Configure registry policy processing: Do not apply during periodic background processing',
        },
    ]
