from core.change_table_module import ChangeTableModule


class CIS_17_5_5(ChangeTableModule):
    """17.5.5 (L1) Ensure 'Audit Other Logon/Logoff Events' is set to include 'Success' and 'Failure'."""

    cis_id = "17.5.5"
    title = "Ensure 'Audit Other Logon/Logoff Events' is set to include 'Success' and 'Failure'"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "auditpol",
            "subcategory_guid": "{0cce921c-69ae-11d9-bed3-505054503030}",
            "success": True,
            "failure": True,
            "label": "Audit Other Logon/Logoff Events = Success and Failure",
        }
    ]
