from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "9.1.4"
    title = "Windows Firewall: Domain: Logging: Name is %SystemRoot%\\System32\\logfiles\\firewall\\domainfw.log"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile\Logging",
            "value_name": "LogFilePath",
            "value_type": "REG_SZ",
            "value": '%SystemRoot%\\System32\\logfiles\\firewall\\domainfw.log',
            "label": "Set firewall log file path (Domain profile)",
        },
    ]
