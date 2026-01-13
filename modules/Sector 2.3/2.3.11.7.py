from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.11.7"
    title = "Network security: LAN Manager authentication level"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\LmCompatibilityLevel",
            "value": "4,5",
            "label": "Set LmCompatibilityLevel=5 (Send NTLMv2 only; refuse LM/NTLM)",
        },
    ]
