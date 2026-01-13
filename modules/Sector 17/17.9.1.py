from core.change_table_module import ChangeTableModule


class CIS_17_9_1(ChangeTableModule):
    """17.9.1 (L1) Ensure 'Audit IPsec Driver' is set to include 'Success and Failure'."""

    cis_id = "17.9.1"
    title = "Ensure 'Audit IPsec Driver' is set to include 'Success and Failure'"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "auditpol",
            "subcategory_guid": "{0cce9213-69ae-11d9-bed3-505054503030}",
            "success": True,
            "failure": True,
            "label": "'Audit IPsec Driver' is set to include 'Success and Failure'",
        }
    ]
