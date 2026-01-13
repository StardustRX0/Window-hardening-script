from core.change_table_module import ChangeTableModule


class CIS18_6_19_2_1(ChangeTableModule):
    """CIS 18.6.19.2.1 (L2)

    Ensure 'TCPIP6 Parameter (Disable IPv6) (DisabledComponents)' is set to '0xff (255)'.

    Warning:
    - Disabling IPv6 can break components that require it. Apply only if your environment
      has explicitly decided to disable IPv6.
    """

    cis_id = "18.6.19.2.1"
    title = "TCPIP6 Parameter (Disable IPv6) (DisabledComponents)"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SYSTEM\CurrentControlSet\Services\Tcpip6\Parameters",
            "value_name": "DisabledComponents",
            "value_type": "REG_DWORD",
            "value": 255,
            "label": "TCPIP6: DisabledComponents",
        },
    ]
