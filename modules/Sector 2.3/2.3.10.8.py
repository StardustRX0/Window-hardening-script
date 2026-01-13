from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.10.8"
    title = "Network access: Remotely accessible registry paths"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\SecurePipeServers\Winreg\AllowedExactPaths\Machine",
            "value": "7,System\CurrentControlSet\Control\ProductOptions,System\CurrentControlSet\Control\Server Applications,Software\Microsoft\Windows NT\CurrentVersion",
            "label": "Remotely accessible registry paths (AllowedExactPaths\Machine)",
        }
    ]
