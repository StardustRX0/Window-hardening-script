from core.change_table_module import ChangeTableModule


class CIS_17_5_1(ChangeTableModule):
    """17.5.1 (L1) Ensure 'Audit Account Lockout' is set to include 'Failure'."""

    cis_id = "17.5.1"
    title = "Ensure 'Audit Account Lockout' is set to include 'Failure'"
    profiles = ["dc", "ms"]

    _changes = [
        {
            "type": "auditpol",
            "subcategory_guid": "{0cce9217-69ae-11d9-bed3-505054503030}",
            "failure": True,
            "label": "Audit Account Lockout = Failure",
        }
    ]
