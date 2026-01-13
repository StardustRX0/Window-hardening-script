from core.change_table_module import ChangeTableModule


class CIS18_6_10_2(ChangeTableModule):
    """CIS 18.6.10.2 (L2)

    Ensure 'Turn off Microsoft Peer-to-Peer Networking Services' is set to 'Enabled'.
    """

    cis_id = "18.6.10.2"
    title = "Turn off Microsoft Peer-to-Peer Networking Services"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Peernet",
            "value_name": "Disabled",
            "value_type": "REG_DWORD",
            "value": 1,
            "label": "Peernet: Disabled",
        },
    ]
