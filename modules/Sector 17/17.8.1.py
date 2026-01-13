from core.change_table_module import ChangeTableModule


class CIS_17_8_1(ChangeTableModule):
    """17.8.1 (L1) Ensure 'Audit Sensitive Privilege Use' is set to include 'Success and Failure'."""

    cis_id = "17.8.1"
    title = "Ensure 'Audit Sensitive Privilege Use' is set to include 'Success and Failure'"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "auditpol",
            "subcategory_guid": "{0cce9228-69ae-11d9-bed3-505054503030}",
            "success": True,
            "failure": True,
            "label": "'Audit Sensitive Privilege Use' is set to include 'Success and Failure'",
        }
    ]
