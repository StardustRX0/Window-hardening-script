from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.17.3"
    title = "User Account Control: Behavior of the elevation prompt for standard users"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\ConsentPromptBehaviorUser",
            "value": "4,0",
            "label": "Set ConsentPromptBehaviorUser=0 (Automatically deny elevation requests)",
        },
    ]
