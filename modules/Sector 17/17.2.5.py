from core.change_table_module import ChangeTableModule


class CIS_17_2_5(ChangeTableModule):
    """17.2.5 (L1) Ensure 'Audit Security Group Management' is set to include 'Success'."""

    cis_id = "17.2.5"
    title = "Ensure 'Audit Security Group Management' is set to include 'Success'"
    profiles = ["dc", "ms"]

    _changes = [
        {
            "type": "auditpol",
            "subcategory_guid": "{0cce9237-69ae-11d9-bed3-505054503030}",
            "success": True,
            "label": "Audit Security Group Management = Success",
        }
    ]
