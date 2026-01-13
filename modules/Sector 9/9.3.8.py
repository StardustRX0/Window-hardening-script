from core.change_table_module import ChangeTableModule


class CIS_9_3_8(ChangeTableModule):
    cis_id = "9.3.8"
    title = "Windows Defender Firewall: Public: Logging: Log dropped packets"
    profiles = ["dc", "ms"]

    CHANGES = [{'kind': 'reg_set', 'key': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\WindowsFirewall\\PublicProfile\\Logging', 'value_name': 'LogDroppedPackets', 'value_type': 'REG_DWORD', 'target_value': 1, 'label': 'Log dropped packets = Yes'}]
