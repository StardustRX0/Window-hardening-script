from core.change_table_module import ChangeTableModule


class CIS_9_3_7(ChangeTableModule):
    cis_id = "9.3.7"
    title = "Windows Defender Firewall: Public: Logging: Size limit (KB)"
    profiles = ["dc", "ms"]

    CHANGES = [{'kind': 'reg_set', 'key': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\WindowsFirewall\\PublicProfile\\Logging', 'value_name': 'LogFileSize', 'value_type': 'REG_DWORD', 'target_value': 16384, 'label': 'Log file size (KB) = 16384'}]
