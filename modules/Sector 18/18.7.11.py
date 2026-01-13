from core.change_table_module import ChangeTableModule


class CIS18_7_11(ChangeTableModule):
    """CIS 18.7.11"""

    cis_id = "18.7.11"
    title = "Point and Print: warn and prompt for elevation on new connections"
    description = 'Shows warning and elevation prompt when installing drivers for a new Point and Print connection. This helps prevent silent driver installation by non-admin users.'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": 'reg_set',
            "key": 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\Printers\\PointAndPrint',
            "value_name": 'NoWarningNoElevationOnInstall',
            "value_type": 'REG_DWORD',
            "value": 0,
            "label": 'Computer Configuration\\Policies\\Administrative Templates\\Printers\\Point and Print Restrictions: When installing drivers for a new connection',
        },
    ]
