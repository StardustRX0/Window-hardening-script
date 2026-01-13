from core.change_table_module import ChangeTableModule


class CIS_17_6_2(ChangeTableModule):
    """17.6.2 (L1) Ensure 'Audit File Share' is set to include 'Success' and 'Failure'."""

    cis_id = "17.6.2"
    title = "Ensure 'Audit File Share' is set to include 'Success' and 'Failure'"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "auditpol",
            "subcategory_guid": "{0cce9224-69ae-11d9-bed3-505054503030}",
            "success": True,
            "failure": True,
            "label": "Audit File Share = Success and Failure",
        }
    ]
