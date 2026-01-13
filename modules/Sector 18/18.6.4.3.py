from core.change_table_module import ChangeTableModule


class CIS18_6_4_3(ChangeTableModule):
    """CIS 18.6.4.3 (L1)

    Ensure 'Turn off default IPv6 DNS Servers' is set to 'Enabled'.
    """

    id = "18.6.4.3"
    title = "Turn off default IPv6 DNS Servers"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient",
            "value_name": "DisableIPv6DefaultDnsServers",
            "value_type": "REG_DWORD",
            "value": 1,
            "label": "Disable IPv6 Default DNS Servers (DisableIPv6DefaultDnsServers=1)",
        }
    ]
