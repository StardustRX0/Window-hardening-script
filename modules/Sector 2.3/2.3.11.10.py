from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.11.10"
    title = "Network security: Minimum session security for NTLM SSP based (including secure RPC) clients"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\MSV1_0\NTLMMinClientSec",
            "value": "4,537395200",
            "label": "Set NTLMMinClientSec=537395200 (Require NTLMv2 session security + 128-bit)",
        },
    ]
