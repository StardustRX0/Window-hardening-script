from core.change_table_module import ChangeTableModule


class CIS_2_3_1_4(ChangeTableModule):
    cis_id = "2.3.1.4"
    title = "Accounts: Rename guest account (Configure)"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "secedit_system_access",
            "key": "NewGuestName",
            # Pull from config: 2.3.1.4 -> name: "<new name>"
            "value_from": "name",
            "label": "Accounts: Rename guest account",
        }
    ]
