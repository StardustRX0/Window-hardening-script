from core.change_table_module import ChangeTableModule


class CIS_2_3_1_2(ChangeTableModule):
    cis_id = "2.3.1.2"
    title = "Accounts: Limit local account use of blank passwords to console logon only (Enabled)"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\LimitBlankPasswordUse",
            # REG_DWORD 1 -> secedit registry format: 4,1
            "value": "4,1",
            "label": "LimitBlankPasswordUse",
        }
    ]
