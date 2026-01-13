from core.change_table_module import ChangeTableModule


class CIS_17_9_5(ChangeTableModule):
    """17.9.5 (L1) Ensure 'Audit System Integrity' is set to include 'Success and Failure'."""

    cis_id = "17.9.5"
    title = "Ensure 'Audit System Integrity' is set to include 'Success and Failure'"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "auditpol",
            "subcategory_guid": "{0cce9212-69ae-11d9-bed3-505054503030}",
            "success": True,
            "failure": True,
            "label": "'Audit System Integrity' is set to include 'Success and Failure'",
        }
    ]
