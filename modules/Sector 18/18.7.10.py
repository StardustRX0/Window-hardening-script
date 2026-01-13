from core.change_table_module import ChangeTableModule


class CIS18_7_10(ChangeTableModule):
    """CIS 18.7.10"""

    cis_id = "18.7.10"
    title = "Manage processing of Queue-specific files"
    description = 'Limits queue-specific files to Color profiles (Point and Print). This reduces the attack surface by restricting what files are processed for print queues.'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": 'reg_set',
            "key": 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\Printers\\PointAndPrint',
            "value_name": 'CopyFilesPolicy',
            "value_type": 'REG_DWORD',
            "value": 1,
            "label": 'Computer Configuration\\Policies\\Administrative Templates\\Printers\\Point and Print Restrictions: Manage processing of Queue-specific files',
        },
    ]
