from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.10.13"
    title = "Network access: Sharing and security model for local accounts"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\ForceGuest",
            "value": "4,0",
            "label": "Set ForceGuest=0 (Classic - local users authenticate as themselves)",
        },
    ]
