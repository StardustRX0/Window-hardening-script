from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.11.12"
    title = "Network security: Restrict NTLM: Audit Incoming NTLM Traffic"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\MSV1_0\AuditReceivingNTLMTraffic",
            "value": "4,2",
            "label": "Set AuditReceivingNTLMTraffic=2 (Enable auditing for all accounts)",
        },
    ]
