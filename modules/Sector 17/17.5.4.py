from core.change_table_module import ChangeTableModule


class CIS_17_5_4(ChangeTableModule):
    """17.5.4 (L1) Ensure 'Audit Logon' is set to include 'Success' and 'Failure'."""

    cis_id = "17.5.4"
    title = "Ensure 'Audit Logon' is set to include 'Success' and 'Failure'"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "auditpol",
            "subcategory_guid": "{0cce9215-69ae-11d9-bed3-505054503030}",
            "success": True,
            "failure": True,
            "label": "Audit Logon = Success and Failure",
        }
    ]
