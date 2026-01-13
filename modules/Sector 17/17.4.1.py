from core.change_table_module import ChangeTableModule


class CIS_17_4_1(ChangeTableModule):
    """17.4.1 (L1) Ensure 'Audit Directory Service Access' is set to include 'Failure' (DC only)."""

    cis_id = "17.4.1"
    title = "Ensure 'Audit Directory Service Access' is set to include 'Failure' (DC only)"
    profiles = ["dc"]

    _changes = [
        {
            "type": "auditpol",
            "subcategory_guid": "{0cce923b-69ae-11d9-bed3-505054503030}",
            "failure": True,
            "label": "Audit Directory Service Access = Failure",
        }
    ]
