from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.17.2"
    title = "User Account Control: Behavior of the elevation prompt for administrators in Admin Approval Mode"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\ConsentPromptBehaviorAdmin",
            "value": "4,2",
            "label": "Set ConsentPromptBehaviorAdmin=2 (Prompt for consent on secure desktop; CIS allows 1 or 2)",
        },
    ]
