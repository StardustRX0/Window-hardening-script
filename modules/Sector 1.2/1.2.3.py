from core.change_table_module import ChangeTableModule


class CIS_1_2_3(ChangeTableModule):
    cis_id = "1.2.3"
    title = 'Admin Lockout'

    CHANGES = [
        {
            "kind": "reg_set",
            "key": 'HKLM\\SYSTEM\\CurrentControlSet\\Control\\Lsa',
            "value_name": 'AllowAdministratorLockout',
            "value_type": "REG_DWORD",
            "value_from": 'admin_lockout',
            "default": 1,
            "label": 'Admin Lockout',
        }
    ]
