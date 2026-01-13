from core.change_table_module import ChangeTableModule


class CIS_18_5_7(ChangeTableModule):
    """18.5.7 Ensure 'MSS: (PerformRouterDiscovery) Allow IRDP to detect and configure Default Gateway addresses'."""

    cis_id = "18.5.7"
    title = "MSS (PerformRouterDiscovery) Allow IRDP to detect and configure Default Gateway addresses"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters",
            "value_name": "PerformRouterDiscovery",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "Disable IRDP router discovery (PerformRouterDiscovery=0)",
        },
    ]
