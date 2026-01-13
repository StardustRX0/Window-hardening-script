from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.11.5"
    title = "Network security: Do not store LAN Manager hash value on next password change"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\NoLMHash",
            "value": "4,1",
            "label": "Set NoLMHash=1 (Enabled)",
        },
    ]
