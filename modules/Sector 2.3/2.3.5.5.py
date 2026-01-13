from core.change_table_module import ChangeTableModule


class CIS_2_3_5_5(ChangeTableModule):
    cis_id = "2.3.5.5"
    title = "Domain controller: Refuse machine account password changes"
    profiles = ["dc"]

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Services\Netlogon\Parameters\RefusePasswordChange",
            "value": "4,0",
            "label": "DC: Refuse machine account password changes (Disabled)",
        }
    ]
