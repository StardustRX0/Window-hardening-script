from core.change_table_module import ChangeTableModule


class CIS_1_1_6(ChangeTableModule):
    cis_id = "1.1.6"
    title = 'Relax Limits'

    CHANGES = [
        {
            "kind": "reg_set",
            "key": 'HKLM\\SYSTEM\\CurrentControlSet\\Control\\SAM',
            "value_name": 'RelaxMinimumPasswordLengthLimits',
            "value_type": "REG_DWORD",
            "value": '1',
            "label": 'Relax Limits',
        }
    ]
