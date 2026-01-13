from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.11.13"
    title = "Network security: Restrict NTLM: Audit NTLM authentication in this domain (DC only)"
    profiles = ['dc']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Services\Netlogon\Parameters\AuditNTLMInDomain",
            "value": "4,7",
            "label": "Set AuditNTLMInDomain=7 (Enable all)",
        },
    ]
