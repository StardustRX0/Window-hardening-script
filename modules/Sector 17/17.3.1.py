from core.change_table_module import ChangeTableModule


class CIS_17_3_1(ChangeTableModule):
    """17.3.1 (L1) Ensure 'Audit PNP Activity' is set to include 'Success'."""

    cis_id = "17.3.1"
    title = "Ensure 'Audit PNP Activity' is set to include 'Success'"
    profiles = ["dc", "ms"]

    _changes = [
        {
            "type": "auditpol",
            "subcategory_guid": "{0cce9248-69ae-11d9-bed3-505054503030}",
            "success": True,
            "label": "Audit PNP Activity = Success",
        }
    ]
