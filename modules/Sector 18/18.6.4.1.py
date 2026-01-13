from core.change_table_module import ChangeTableModule


class CIS18_6_4_1(ChangeTableModule):
    """CIS 18.6.4.1 (L1)

    Ensure 'Configure multicast DNS (mDNS) protocol' is set to 'Disabled'.
    """

    id = "18.6.4.1"
    title = "Configure multicast DNS (mDNS) protocol"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient",
            "value_name": "EnableMDNS",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "Disable mDNS (EnableMDNS=0)",
        }
    ]
