from core.change_table_module import ChangeTableModule


class CIS_18_4_6(ChangeTableModule):
    """18.4.6 Ensure 'NetBT NodeType configuration (P-node)'."""

    cis_id = "18.4.6"
    title = "NetBT NodeType configuration (P-node)"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "reg_set",
            "key": "HKLM\\SYSTEM\\CurrentControlSet\\Services\\NetBT\\Parameters",
            "value_name": "NodeType",
            "value_type": "REG_DWORD",
            "value": 2,
            "label": "Set NetBT NodeType to P-node (NodeType=2)",
        },
    ]
