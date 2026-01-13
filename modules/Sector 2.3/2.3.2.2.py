from core.change_table_module import ChangeTableModule


class CIS_2_3_2_2(ChangeTableModule):
    cis_id = "2.3.2.2"
    title = "Audit: Shut down system immediately if unable to log security audits"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\CrashOnAuditFail",
            "value": "4,0",
            "label": "Audit: CrashOnAuditFail (Disabled)",
        }
    ]
