from core.change_table_module import ChangeTableModule


class CIS_17_7_2(ChangeTableModule):
    """17.7.2 (L1) Ensure 'Audit Authentication Policy Change' is set to include 'Success'."""

    cis_id = "17.7.2"
    title = "Ensure 'Audit Authentication Policy Change' is set to include 'Success'"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "auditpol",
            "subcategory_guid": "{0cce9230-69ae-11d9-bed3-505054503030}",
            "success": True,
            "failure": False,
            "label": "Audit Authentication Policy Change = Success",
        }
    ]
