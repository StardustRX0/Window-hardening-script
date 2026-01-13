from core.change_table_module import ChangeTableModule


class CIS18_6_20_2(ChangeTableModule):
    """CIS 18.6.20.2 (L2)

    Ensure 'Prohibit access of the Windows Connect Now wizards' is set to 'Enabled'.
    """

    cis_id = "18.6.20.2"
    title = "Prohibit access of the Windows Connect Now wizards"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\WCN\UI",
            "value_name": "DisableWcnUi",
            "value_type": "REG_DWORD",
            "value": 1,
            "label": "WCN UI: DisableWcnUi",
        },
    ]
