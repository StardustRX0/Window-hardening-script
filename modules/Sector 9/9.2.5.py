from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "9.2.5"
    title = "Windows Firewall: Private: Logging: Size limit (KB) is 16,384 KB or greater"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall\PrivateProfile\Logging",
            "value_name": "LogFileSize",
            "value_type": "REG_DWORD",
            "value": 16384,
            "label": "Set firewall log size (Private profile)",
        },
    ]
