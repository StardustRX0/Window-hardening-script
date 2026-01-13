from core.change_table_module import ChangeTableModule


class CIS_17_2_3(ChangeTableModule):
    """17.2.3 (L1) Ensure 'Audit Distribution Group Management' is set to include 'Success' (DC only)."""

    cis_id = "17.2.3"
    title = "Ensure 'Audit Distribution Group Management' is set to include 'Success' (DC only)"
    profiles = ["dc"]

    _changes = [
        {
            "type": "auditpol",
            "subcategory_guid": "{0cce9238-69ae-11d9-bed3-505054503030}",
            "success": True,
            "label": "Audit Distribution Group Management = Success",
        }
    ]
