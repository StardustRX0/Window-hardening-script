from core.change_table_module import ChangeTableModule


class CIS_18_5_8(ChangeTableModule):
    """18.5.8 Ensure 'MSS: (SafeDllSearchMode) Enable Safe DLL search mode'."""

    cis_id = "18.5.8"
    title = "MSS (SafeDllSearchMode) Enable Safe DLL search mode"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager",
            "value_name": "SafeDllSearchMode",
            "value_type": "REG_DWORD",
            "value": 1,
            "label": "Enable Safe DLL search mode (SafeDllSearchMode=1)",
        },
    ]
