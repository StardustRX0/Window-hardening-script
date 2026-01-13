from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.11.2"
    title = "Network security: Allow LocalSystem NULL session fallback"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\MSV1_0\AllowNullSessionFallback",
            "value": "4,0",
            "label": "Set AllowNullSessionFallback=0 (Disabled)",
        },
    ]
