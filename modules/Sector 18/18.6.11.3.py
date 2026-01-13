from core.change_table_module import ChangeTableModule


class CIS18_6_11_3(ChangeTableModule):
    """CIS 18.6.11.3 (L1)

    Ensure 'Prohibit use of Internet Connection Sharing on your DNS domain network'
    is set to 'Enabled'.
    """

    cis_id = "18.6.11.3"
    title = "Prohibit use of Internet Connection Sharing on your DNS domain network"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\Network Connections",
            "value_name": "NC_ShowSharedAccessUI",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "Network Connections: NC_ShowSharedAccessUI",
        },
    ]
