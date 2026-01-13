from core.change_table_module import ChangeTableModule


class CIS18_6_14_1(ChangeTableModule):
    """CIS 18.6.14.1 (L1)

    Ensure 'Hardened UNC Paths' is set to 'Enabled, with "Require Mutual Authentication" and
    "Require Integrity" set for all NETLOGON and SYSVOL shares'.

    Note:
    - This control writes REG_SZ values under HardenedPaths for \\*\\NETLOGON and \\*\\SYSVOL.
    """

    cis_id = "18.6.14.1"
    title = "Hardened UNC Paths"
    profiles = ["dc", "ms"]

    _HARDENED_VALUE = "RequireMutualAuthentication=1, RequireIntegrity=1, RequirePrivacy=1"

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\NetworkProvider\HardenedPaths",
            "value_name": "\\\\*\\\\NETLOGON",
            "value_type": "REG_SZ",
            "value": _HARDENED_VALUE,
            "label": "HardenedPaths: \\\\*\\NETLOGON",
        },
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\NetworkProvider\HardenedPaths",
            "value_name": "\\\\*\\\\SYSVOL",
            "value_type": "REG_SZ",
            "value": _HARDENED_VALUE,
            "label": "HardenedPaths: \\\\*\\SYSVOL",
        },
    ]
