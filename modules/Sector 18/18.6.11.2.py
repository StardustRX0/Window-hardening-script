from core.change_table_module import ChangeTableModule


class CIS18_6_11_2(ChangeTableModule):
    """CIS 18.6.11.2 (L1)

    Ensure 'Prohibit installation and configuration of Network Bridge on your DNS domain network'
    is set to 'Enabled'.
    """

    cis_id = "18.6.11.2"
    title = "Prohibit installation and configuration of Network Bridge on your DNS domain network"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\Network Connections",
            "value_name": "NC_AllowNetBridge_NLA",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "Network Connections: NC_AllowNetBridge_NLA",
        },
    ]
