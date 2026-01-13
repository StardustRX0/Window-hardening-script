from core.change_table_module import ChangeTableModule


class CIS18_5_11(ChangeTableModule):
    """CIS 18.5.11 (L2) - MSS (Legacy)

    Ensure 'MSS: (TcpMaxDataRetransmissions) How many times unacknowledged data is retransmitted'
    is set to 'Enabled: 3'.
    """

    id = "18.5.11"
    title = "MSS: (TcpMaxDataRetransmissions) How many times unacknowledged data is retransmitted"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters",
            "value_name": "TcpMaxDataRetransmissions",
            "value_type": "REG_DWORD",
            "value": 3,
            "label": "TcpMaxDataRetransmissions (IPv4)",
        }
    ]
