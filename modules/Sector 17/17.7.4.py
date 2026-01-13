from core.change_table_module import ChangeTableModule


class CIS_17_7_4(ChangeTableModule):
    """17.7.4 (L1) Ensure 'Audit MPSSVC Rule-Level Policy Change' is set to include 'Success and Failure'."""

    cis_id = "17.7.4"
    title = "Ensure 'Audit MPSSVC Rule-Level Policy Change' is set to include 'Success and Failure'"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "auditpol",
            "subcategory_guid": "{0cce9232-69ae-11d9-bed3-505054503030}",
            "success": True,
            "failure": True,
            "label": "'Audit MPSSVC Rule-Level Policy Change' is set to include 'Success and Failure'",
        }
    ]
