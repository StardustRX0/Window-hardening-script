from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "9.1.1"
    title = "Windows Firewall: Domain: Firewall state is On (recommended)"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile",
            "value_name": "EnableFirewall",
            "value_type": "REG_DWORD",
            "value": 1,
            "label": "Enable Windows Firewall for Domain profile",
        },
    ]
