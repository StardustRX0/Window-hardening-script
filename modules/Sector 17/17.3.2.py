from core.change_table_module import ChangeTableModule


class CIS_17_3_2(ChangeTableModule):
    """17.3.2 (L1) Ensure 'Audit Process Creation' is set to include 'Success'."""

    cis_id = "17.3.2"
    title = "Ensure 'Audit Process Creation' is set to include 'Success'"
    profiles = ["dc", "ms"]

    _changes = [
        {
            "type": "auditpol",
            "subcategory_guid": "{0cce922b-69ae-11d9-bed3-505054503030}",
            "success": True,
            "label": "Audit Process Creation = Success",
        }
    ]
