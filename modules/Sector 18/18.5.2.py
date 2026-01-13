from core.change_table_module import ChangeTableModule


class CIS_18_5_2(ChangeTableModule):
    """18.5.2 Ensure 'MSS: (DisableIPSourceRouting IPv6) IP source routing protection level'."""

    cis_id = "18.5.2"
    title = "MSS (DisableIPSourceRouting IPv6) IP source routing protection level"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip6\\Parameters",
            "value_name": "DisableIPSourceRouting",
            "value_type": "REG_DWORD",
            "value": 2,
            "label": "Disable IPv6 source routing (DisableIPSourceRouting=2)",
        },
    ]
