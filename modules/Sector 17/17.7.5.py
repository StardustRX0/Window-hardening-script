from core.change_table_module import ChangeTableModule


class CIS_17_7_5(ChangeTableModule):
    """17.7.5 (L1) Ensure 'Audit Other Policy Change Events' is set to include 'Failure'."""

    cis_id = "17.7.5"
    title = "Ensure 'Audit Other Policy Change Events' is set to include 'Failure'"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "auditpol",
            "subcategory_guid": "{0cce9234-69ae-11d9-bed3-505054503030}",
            "success": False,
            "failure": True,
            "label": "'Audit Other Policy Change Events' is set to include 'Failure'",
        }
    ]
