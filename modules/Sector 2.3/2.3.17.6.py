from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.17.6"
    title = "User Account Control: Run all administrators in Admin Approval Mode"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\EnableLUA",
            "value": "4,1",
            "label": "Set EnableLUA=1 (Enabled)",
        },
    ]
