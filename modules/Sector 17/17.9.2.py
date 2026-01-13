from core.change_table_module import ChangeTableModule


class CIS_17_9_2(ChangeTableModule):
    """17.9.2 (L1) Ensure 'Audit Other System Events' is set to include 'Success and Failure'."""

    cis_id = "17.9.2"
    title = "Ensure 'Audit Other System Events' is set to include 'Success and Failure'"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "auditpol",
            "subcategory_guid": "{0cce9214-69ae-11d9-bed3-505054503030}",
            "success": True,
            "failure": True,
            "label": "'Audit Other System Events' is set to include 'Success and Failure'",
        }
    ]
