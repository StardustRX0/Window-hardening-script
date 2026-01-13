from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.15.1"
    title = "System objects: Require case insensitivity for non-Windows subsystems"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Session Manager\Kernel\ObCaseInsensitive",
            "value": "4,1",
            "label": "Set ObCaseInsensitive=1 (Enabled)",
        },
    ]
