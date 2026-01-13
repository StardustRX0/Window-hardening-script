from core.change_table_module import ChangeTableModule


class CIS_2_3_6_1(ChangeTableModule):
    cis_id = "2.3.6.1"
    title = "Domain member: Digitally encrypt or sign secure channel data (always)"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Services\Netlogon\Parameters\RequireSignOrSeal",
            "value": "4,1",
            "label": "Domain member: Require sign or seal (always)",
        }
    ]
