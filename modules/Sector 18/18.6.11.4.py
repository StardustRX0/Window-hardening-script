from core.change_table_module import ChangeTableModule


class CIS18_6_11_4(ChangeTableModule):
    """CIS 18.6.11.4 (L1)

    Ensure 'Require domain users to elevate when setting a network's location'
    is set to 'Enabled'.
    """

    cis_id = "18.6.11.4"
    title = "Require domain users to elevate when setting a network's location"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\Network Connections",
            "value_name": "NC_StdDomainUserSetLocation",
            "value_type": "REG_DWORD",
            "value": 1,
            "label": "Network Connections: NC_StdDomainUserSetLocation",
        },
    ]
