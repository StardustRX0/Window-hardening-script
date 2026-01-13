from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "9.2.2"
    title = "Windows Firewall: Private: Inbound connections is Block (default)"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall\PrivateProfile",
            "value_name": "DefaultInboundAction",
            "value_type": "REG_DWORD",
            "value": 1,
            "label": "Block inbound connections by default (Private profile)",
        },
    ]
