from core.change_table_module import ChangeTableModule


class CIS18_6_4_2(ChangeTableModule):
    """CIS 18.6.4.2 (L1)

    Ensure 'Configure NetBIOS settings' is set to 'Enabled: Disable NetBIOS name resolution on public networks'.
    """

    id = "18.6.4.2"
    title = "Configure NetBIOS settings"
    profiles = ["dc", "ms"]

    # CIS indicates compliance when EnableNetbios is 0 or 2; we set 2 (disable on public networks)
    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient",
            "value_name": "EnableNetbios",
            "value_type": "REG_DWORD",
            "value": 2,
            "label": "Disable NetBIOS name resolution on public networks (EnableNetbios=2)",
        }
    ]
