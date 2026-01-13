from core.change_table_module import ChangeTableModule


class CIS_18_5_4(ChangeTableModule):
    """18.5.4 Ensure 'MSS: (EnableICMPRedirect) Allow ICMP redirects to override OSPF generated routes'."""

    cis_id = "18.5.4"
    title = "MSS (EnableICMPRedirect) Allow ICMP redirects to override OSPF generated routes"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters",
            "value_name": "EnableICMPRedirect",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "Disable ICMP redirects overriding OSPF routes (EnableICMPRedirect=0)",
        },
    ]
