from core.change_table_module import ChangeTableModule


class CIS_17_5_6(ChangeTableModule):
    """17.5.6 (L1) Ensure 'Audit Special Logon' is set to include 'Success'."""

    cis_id = "17.5.6"
    title = "Ensure 'Audit Special Logon' is set to include 'Success'"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "auditpol",
            "subcategory_guid": "{0cce921b-69ae-11d9-bed3-505054503030}",
            "success": True,
            "failure": False,
            "label": "Audit Special Logon = Success",
        }
    ]
