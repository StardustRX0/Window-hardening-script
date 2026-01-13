from core.change_table_module import ChangeTableModule


class CIS18_7_9(ChangeTableModule):
    """CIS 18.7.9"""

    cis_id = "18.7.9"
    title = "Limits print driver installation to Administrators"
    description = 'Limits print driver installation to Administrators (Point and Print). This reduces the risk of non-admin users installing malicious print drivers.'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": 'reg_set',
            "key": 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\Printers\\PointAndPrint',
            "value_name": 'RestrictDriverInstallationToAdministrators',
            "value_type": 'REG_DWORD',
            "value": 1,
            "label": 'Computer Configuration\\Policies\\Administrative Templates\\Printers\\Point and Print Restrictions: Limits print driver installation to Administrators',
        },
    ]
