from core.change_table_module import ChangeTableModule


class CIS_18_5_5(ChangeTableModule):
    """18.5.5 Ensure 'MSS: (KeepAliveTime) How often keep-alive packets are sent in milliseconds'."""

    cis_id = "18.5.5"
    title = "MSS (KeepAliveTime) How often keep-alive packets are sent in milliseconds"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters",
            "value_name": "KeepAliveTime",
            "value_type": "REG_DWORD",
            "value": 300000,
            "label": "Set TCP keep-alive time to 300,000 ms (KeepAliveTime=300000)",
        },
    ]
