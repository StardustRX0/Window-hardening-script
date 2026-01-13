from core.change_table_module import ChangeTableModule


class CIS_17_5_2(ChangeTableModule):
    """17.5.2 (L1) Ensure 'Audit Group Membership' is set to include 'Success'."""

    cis_id = "17.5.2"
    title = "Ensure 'Audit Group Membership' is set to include 'Success'"
    profiles = ["dc", "ms"]

    _changes = [
        {
            "type": "auditpol",
            "subcategory_guid": "{0cce9249-69ae-11d9-bed3-505054503030}",
            "success": True,
            "label": "Audit Group Membership = Success",
        }
    ]
