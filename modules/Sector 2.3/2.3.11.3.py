from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.11.3"
    title = "Network security: Allow PKU2U authentication requests to this computer to use online identities"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\pku2u\AllowOnlineID",
            "value": "4,0",
            "label": "Set AllowOnlineID=0 (Disabled)",
        },
    ]
