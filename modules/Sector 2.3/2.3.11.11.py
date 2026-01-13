from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.11.11"
    title = "Network security: Minimum session security for NTLM SSP based (including secure RPC) servers"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\MSV1_0\NTLMMinServerSec",
            "value": "4,537395200",
            "label": "Set NTLMMinServerSec=537395200 (Require NTLMv2 session security + 128-bit)",
        },
    ]
