from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.10.5"
    title = "Network access: Let Everyone permissions apply to anonymous users"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\EveryoneIncludesAnonymous",
            "value": "4,0",
            "label": "Let Everyone permissions apply to anonymous users (Disabled)",
        }
    ]
