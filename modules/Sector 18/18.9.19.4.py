from core.change_table_module import ChangeTableModule


class CIS18_9_19_4(ChangeTableModule):
    """CIS 18.9.19.4"""

    cis_id = "18.9.19.4"
    title = "Configure security policy processing: Do not apply during periodic background processing (FALSE)"
    description = "Ensures security policy settings refresh in the background by keeping 'Do not apply during periodic background processing' unchecked."
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": 'reg_set',
            "key": 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Group Policy\\{827D319E-6EAC-11D2-A4EA-00C04F79F83A}',
            "value_name": 'NoBackgroundPolicy',
            "value_type": 'REG_DWORD',
            "value": 0,
            "label": 'Computer Configuration\\Policies\\Administrative Templates\\System\\Group Policy\\Configure security policy processing: Do not apply during periodic background processing',
        },
    ]
