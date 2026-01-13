from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.11.14"
    title = "Network security: Restrict NTLM: Outgoing NTLM traffic to remote servers"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\MSV1_0\RestrictSendingNTLMTraffic",
            "value": "4,1",
            "label": "Set RestrictSendingNTLMTraffic=1 (Audit all)",
        },
    ]
