from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "9.3.1"
    title = "Windows Firewall: Public: Firewall state is On (recommended)"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile",
            "value_name": "EnableFirewall",
            "value_type": "REG_DWORD",
            "value": 1,
            "label": "Enable Windows Firewall for Public profile",
        },
    ]
