from core.change_table_module import ChangeTableModule


class CIS_17_7_3(ChangeTableModule):
    """17.7.3 (L1) Ensure 'Audit Authorization Policy Change' is set to include 'Success'."""

    cis_id = "17.7.3"
    title = "Ensure 'Audit Authorization Policy Change' is set to include 'Success'"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "auditpol",
            "subcategory_guid": "{0cce9231-69ae-11d9-bed3-505054503030}",
            "success": True,
            "failure": False,
            "label": "'Audit Authorization Policy Change' is set to include 'Success'",
        }
    ]
