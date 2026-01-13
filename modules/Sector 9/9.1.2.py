from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "9.1.2"
    title = "Windows Firewall: Domain: Inbound connections is Block (default)"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile",
            "value_name": "DefaultInboundAction",
            "value_type": "REG_DWORD",
            "value": 1,
            "label": "Block inbound connections by default (Domain profile)",
        },
    ]
