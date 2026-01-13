from core.change_table_module import ChangeTableModule


class CIS_9_3_5(ChangeTableModule):
    cis_id = "9.3.5"
    title = "Windows Defender Firewall: Public: Apply local connection security rules"
    profiles = ["dc", "ms"]

    CHANGES = [{'kind': 'reg_set', 'key': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\WindowsFirewall\\PublicProfile', 'value_name': 'AllowLocalIPsecPolicyMerge', 'value_type': 'REG_DWORD', 'target_value': 0, 'label': 'Apply local connection security rules = No'}]
