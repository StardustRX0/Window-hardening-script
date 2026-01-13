from core.change_table_module import ChangeTableModule


class CIS18_6_5_1(ChangeTableModule):
    """CIS 18.6.5.1 (L2)

    Ensure 'Enable Font Providers' is set to 'Disabled'.
    """

    id = "18.6.5.1"
    title = "Enable Font Providers"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\System",
            "value_name": "EnableFontProviders",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "Disable Font Providers (EnableFontProviders=0)",
        }
    ]
