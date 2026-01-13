from core.change_table_module import ChangeTableModule


class CIS_18_5_1(ChangeTableModule):
    """18.5.1 Ensure 'MSS: (AutoAdminLogon) Enable Automatic Logon' is set to 'Disabled'."""

    cis_id = "18.5.1"
    title = "MSS (AutoAdminLogon) Enable Automatic Logon"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",
            "value_name": "AutoAdminLogon",
            "value_type": "REG_SZ",
            "value": "0",
            "label": "Disable automatic logon (AutoAdminLogon=0)",
        },
    ]
