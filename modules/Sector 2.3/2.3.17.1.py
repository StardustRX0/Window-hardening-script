from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.17.1"
    title = "User Account Control: Admin Approval Mode for the Built-in Administrator account"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\FilterAdministratorToken",
            "value": "4,1",
            "label": "Set FilterAdministratorToken=1 (Enabled)",
        },
    ]
