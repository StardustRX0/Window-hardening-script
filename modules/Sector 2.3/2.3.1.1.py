from core.change_table_module import ChangeTableModule


class CIS_2_3_1_1(ChangeTableModule):
    cis_id = "2.3.1.1"
    title = "Accounts: Guest account status (Disabled)"
    profiles = ["ms"]  # MS only (Domain Controllers have no local Guest account)

    CHANGES = [
        {
            "kind": "secedit_system_access",
            "key": "EnableGuestAccount",
            "value": "0",
            "label": "Accounts: Guest account status",
        }
    ]
