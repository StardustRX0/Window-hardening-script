from core.change_table_module import ChangeTableModule


class CIS_17_7_1(ChangeTableModule):
    """17.7.1 (L1) Ensure 'Audit Audit Policy Change' is set to include 'Success'."""

    cis_id = "17.7.1"
    title = "Ensure 'Audit Audit Policy Change' is set to include 'Success'"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "auditpol",
            "subcategory_guid": "{0cce922f-69ae-11d9-bed3-505054503030}",
            "success": True,
            "failure": False,
            "label": "Audit Audit Policy Change = Success",
        }
    ]
