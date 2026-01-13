from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.15.2"
    title = "System objects: Strengthen default permissions of internal system objects (e.g. Symbolic Links)"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Session Manager\ProtectionMode",
            "value": "4,1",
            "label": "Set ProtectionMode=1 (Enabled)",
        },
    ]
