from core.change_table_module import ChangeTableModule


class CIS_17_6_1(ChangeTableModule):
    """17.6.1 (L1) Ensure 'Audit Detailed File Share' is set to include 'Failure'."""

    cis_id = "17.6.1"
    title = "Ensure 'Audit Detailed File Share' is set to include 'Failure'"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "auditpol",
            "subcategory_guid": "{0cce9244-69ae-11d9-bed3-505054503030}",
            "success": False,
            "failure": True,
            "label": "Audit Detailed File Share = Failure",
        }
    ]
