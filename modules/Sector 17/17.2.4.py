from core.change_table_module import ChangeTableModule


class CIS_17_2_4(ChangeTableModule):
    """17.2.4 (L1) Ensure 'Audit Other Account Management Events' is set to include 'Success' (DC only)."""

    cis_id = "17.2.4"
    title = "Ensure 'Audit Other Account Management Events' is set to include 'Success' (DC only)"
    profiles = ["dc"]

    _changes = [
        {
            "type": "auditpol",
            "subcategory_guid": "{0cce923a-69ae-11d9-bed3-505054503030}",
            "success": True,
            "label": "Audit Other Account Management Events = Success",
        }
    ]
