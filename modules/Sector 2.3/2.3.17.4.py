from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.17.4"
    title = "User Account Control: Detect application installations and prompt for elevation"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\EnableInstallerDetection",
            "value": "4,1",
            "label": "Set EnableInstallerDetection=1 (Enabled)",
        },
    ]
