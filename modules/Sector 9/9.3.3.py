from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "9.3.3"
    title = "Windows Firewall: Public: Settings: Display a notification is No"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile",
            "value_name": "DisableNotifications",
            "value_type": "REG_DWORD",
            "value": 1,
            "label": "Disable firewall notifications (Public profile)",
        },
    ]
