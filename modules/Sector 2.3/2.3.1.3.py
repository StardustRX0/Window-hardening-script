from core.change_table_module import ChangeTableModule


class CIS_2_3_1_3(ChangeTableModule):
    cis_id = "2.3.1.3"
    title = "Accounts: Rename administrator account (Configure)"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "secedit_system_access",
            "key": "NewAdministratorName",
            # Pull from config: 2.3.1.3 -> name: "<new name>"
            "value_from": "name",
            "label": "Accounts: Rename administrator account",
        }
    ]
