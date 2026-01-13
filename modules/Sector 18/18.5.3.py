from core.change_table_module import ChangeTableModule


class CIS_18_5_3(ChangeTableModule):
    """18.5.3 Ensure 'MSS: (DisableIPSourceRouting) IP source routing protection level'."""

    cis_id = "18.5.3"
    title = "MSS (DisableIPSourceRouting) IP source routing protection level"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters",
            "value_name": "DisableIPSourceRouting",
            "value_type": "REG_DWORD",
            "value": 2,
            "label": "Disable IPv4 source routing (DisableIPSourceRouting=2)",
        },
    ]
