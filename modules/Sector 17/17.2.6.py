from core.change_table_module import ChangeTableModule


class CIS_17_2_6(ChangeTableModule):
    """17.2.6 (L1) Ensure 'Audit User Account Management' is set to 'Success and Failure'."""

    cis_id = "17.2.6"
    title = "Ensure 'Audit User Account Management' is set to 'Success and Failure'"
    profiles = ["dc", "ms"]

    _changes = [
        {
            "type": "auditpol",
            "subcategory_guid": "{0cce9235-69ae-11d9-bed3-505054503030}",
            "success": True,
            "failure": True,
            "label": "Audit User Account Management = Success and Failure",
        }
    ]
