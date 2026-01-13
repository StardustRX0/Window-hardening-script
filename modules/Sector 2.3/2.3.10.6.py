from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.10.6"
    title = "Network access: Named Pipes that can be accessed anonymously"
    profiles = ['dc']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\NullSessionPipes",
            "value": "7,LSARPC,NETLOGON,SAMR",
            "label": "Named Pipes that can be accessed anonymously (DC default allowlist)",
        }
    ]
