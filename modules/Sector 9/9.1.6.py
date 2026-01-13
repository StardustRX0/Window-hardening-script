from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "9.1.6"
    title = "Windows Firewall: Domain: Logging: Log dropped packets is Yes"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile\Logging",
            "value_name": "LogDroppedPackets",
            "value_type": "REG_DWORD",
            "value": 1,
            "label": "Enable logging of dropped packets (Domain profile)",
        },
    ]
