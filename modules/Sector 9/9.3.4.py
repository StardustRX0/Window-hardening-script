from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "9.3.4"
    title = "Windows Firewall: Public: Settings: Apply local firewall rules is No"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile",
            "value_name": "AllowLocalPolicyMerge",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "Do not apply local firewall rules (Public profile)",
        },
    ]
