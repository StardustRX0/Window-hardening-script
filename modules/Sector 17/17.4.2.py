from core.change_table_module import ChangeTableModule


class CIS_17_4_2(ChangeTableModule):
    """17.4.2 (L1) Ensure 'Audit Directory Service Changes' is set to include 'Success' (DC only)."""

    cis_id = "17.4.2"
    title = "Ensure 'Audit Directory Service Changes' is set to include 'Success' (DC only)"
    profiles = ["dc"]

    _changes = [
        {
            "type": "auditpol",
            "subcategory_guid": "{0cce923c-69ae-11d9-bed3-505054503030}",
            "success": True,
            "label": "Audit Directory Service Changes = Success",
        }
    ]
