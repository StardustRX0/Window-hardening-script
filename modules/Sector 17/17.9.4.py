from core.change_table_module import ChangeTableModule


class CIS_17_9_4(ChangeTableModule):
    """17.9.4 (L1) Ensure 'Audit Security System Extension' is set to include 'Success and Failure'."""

    cis_id = "17.9.4"
    title = "Ensure 'Audit Security System Extension' is set to include 'Success and Failure'"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "auditpol",
            "subcategory_guid": "{0cce9211-69ae-11d9-bed3-505054503030}",
            "success": True,
            "failure": True,
            "label": "'Audit Security System Extension' is set to include 'Success and Failure'",
        }
    ]
