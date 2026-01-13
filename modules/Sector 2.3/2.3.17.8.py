from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.17.8"
    title = "User Account Control: Virtualize file and registry write failures to per-user locations"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\EnableVirtualization",
            "value": "4,1",
            "label": "Set EnableVirtualization=1 (Enabled)",
        },
    ]
