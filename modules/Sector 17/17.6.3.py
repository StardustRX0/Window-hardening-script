from core.change_table_module import ChangeTableModule


class CIS_17_6_3(ChangeTableModule):
    """17.6.3 (L1) Ensure 'Audit Other Object Access Events' is set to include 'Success' and 'Failure'."""

    cis_id = "17.6.3"
    title = "Ensure 'Audit Other Object Access Events' is set to include 'Success' and 'Failure'"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "auditpol",
            "subcategory_guid": "{0cce9227-69ae-11d9-bed3-505054503030}",
            "success": True,
            "failure": True,
            "label": "Audit Other Object Access Events = Success and Failure",
        }
    ]
