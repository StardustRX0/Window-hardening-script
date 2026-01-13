from core.change_table_module import ChangeTableModule


class CIS_2_3_2_1(ChangeTableModule):
    cis_id = "2.3.2.1"
    title = "Audit: Force audit policy subcategory settings to override audit policy category settings"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\SCENoApplyLegacyAuditPolicy",
            "value": "4,1",
            "label": "Audit: Force audit subcategory policy",
        }
    ]
