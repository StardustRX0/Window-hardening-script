from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.10.1"
    title = "Network access: Allow anonymous SID/Name translation"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\TurnOffAnonymousBlock",
            "value": "4,1",
            "label": "Allow anonymous SID/Name translation (Disabled)",
        }
    ]
