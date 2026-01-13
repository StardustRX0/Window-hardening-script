from core.change_table_module import ChangeTableModule


class CIS_17_6_4(ChangeTableModule):
    """17.6.4 (L1) Ensure 'Audit Removable Storage' is set to include 'Success' and 'Failure'."""

    cis_id = "17.6.4"
    title = "Ensure 'Audit Removable Storage' is set to include 'Success' and 'Failure'"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "auditpol",
            "subcategory_guid": "{0cce9245-69ae-11d9-bed3-505054503030}",
            "success": True,
            "failure": True,
            "label": "Audit Removable Storage = Success and Failure",
        }
    ]
