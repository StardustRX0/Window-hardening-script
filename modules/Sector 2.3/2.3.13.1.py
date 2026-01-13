from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.13.1"
    title = "Shutdown: Allow system to be shut down without having to log on"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\ShutdownWithoutLogon",
            "value": "4,0",
            "label": "Set ShutdownWithoutLogon=0 (Disabled)",
        },
    ]
