from core.change_table_module import ChangeTableModule


class CIS_9_3_6(ChangeTableModule):
    cis_id = "9.3.6"
    title = "Windows Defender Firewall: Public: Logging: Name"
    profiles = ["dc", "ms"]

    CHANGES = [{'kind': 'reg_set', 'key': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\WindowsFirewall\\PublicProfile\\Logging', 'value_name': 'LogFilePath', 'value_type': 'REG_SZ', 'target_value': '%SystemRoot%\\System32\\logfiles\\firewall\\publicfw.log', 'label': 'Logging name = %SystemRoot%\\System32\\logfiles\\firewall\\publicfw.log'}]
