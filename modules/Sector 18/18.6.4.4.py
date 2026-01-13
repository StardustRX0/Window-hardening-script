from core.change_table_module import ChangeTableModule


class CIS18_6_4_4(ChangeTableModule):
    """CIS 18.6.4.4 (L1)

    Ensure 'Turn off multicast name resolution' is set to 'Enabled'.
    (Disables Link-Local Multicast Name Resolution / LLMNR.)
    """

    id = "18.6.4.4"
    title = "Turn off multicast name resolution"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient",
            "value_name": "EnableMulticast",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "Turn off LLMNR (EnableMulticast=0)",
        }
    ]
