from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.17.7"
    title = "User Account Control: Switch to the secure desktop when prompting for elevation"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\PromptOnSecureDesktop",
            "value": "4,1",
            "label": "Set PromptOnSecureDesktop=1 (Enabled)",
        },
    ]
