from core.change_table_module import ChangeTableModule


class CIS_17_5_3(ChangeTableModule):
    """17.5.3 (L1) Ensure 'Audit Logoff' is set to include 'Success'."""

    cis_id = "17.5.3"
    title = "Ensure 'Audit Logoff' is set to include 'Success'"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "auditpol",
            "subcategory_guid": "{0cce9216-69ae-11d9-bed3-505054503030}",
            "success": True,
            "failure": False,
            "label": "Audit Logoff = Success",
        }
    ]
