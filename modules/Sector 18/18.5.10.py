from core.change_table_module import ChangeTableModule


class CIS_18_5_10(ChangeTableModule):
    """18.5.10 Ensure 'MSS: (TcpMaxDataRetransmissions IPv6) How many times unacknowledged data is retransmitted'."""

    cis_id = "18.5.10"
    title = "MSS (TcpMaxDataRetransmissions IPv6) How many times unacknowledged data is retransmitted"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": "HKLM\\SYSTEM\\CurrentControlSet\\Services\\TCPIP6\\Parameters",
            "value_name": "TcpMaxDataRetransmissions",
            "value_type": "REG_DWORD",
            "value": 3,
            "label": "Set IPv6 TCP max data retransmissions to 3 (TcpMaxDataRetransmissions=3)",
        },
    ]
