from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "9.2.4"
    title = "Windows Firewall: Private: Logging: Name is %SystemRoot%\\System32\\logfiles\\firewall\\privatefw.log"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall\PrivateProfile\Logging",
            "value_name": "LogFilePath",
            "value_type": "REG_SZ",
            "value": "%SystemRoot%\\System32\\logfiles\\firewall\\privatefw.log",
            "label": "Set firewall log file path (Private profile)",
        },
    ]
