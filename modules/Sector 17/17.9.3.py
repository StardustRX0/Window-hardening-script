from core.change_table_module import ChangeTableModule


class CIS_17_9_3(ChangeTableModule):
    """17.9.3 (L1) Ensure 'Audit Security State Change' is set to include 'Success'."""

    cis_id = "17.9.3"
    title = "Ensure 'Audit Security State Change' is set to include 'Success'"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "auditpol",
            "subcategory_guid": "{0cce9210-69ae-11d9-bed3-505054503030}",
            "success": True,
            "failure": False,
            "label": "'Audit Security State Change' is set to include 'Success'",
        }
    ]
