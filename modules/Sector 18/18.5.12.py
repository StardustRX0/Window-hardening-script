from core.change_table_module import ChangeTableModule


class CIS18_5_12(ChangeTableModule):
    """CIS 18.5.12 (L1) - MSS (Legacy)

    Ensure 'MSS: (WarningLevel) Percentage threshold for the security event log at which the system
    will generate a warning' is set to 'Enabled: 90 or less'.
    """

    id = "18.5.12"
    title = "MSS: (WarningLevel) Percentage threshold for the security event log at which the system will generate a warning"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SYSTEM\CurrentControlSet\Services\Eventlog\Security",
            "value_name": "WarningLevel",
            "value_type": "REG_DWORD",
            "value": 90,
            "label": "Security Event Log WarningLevel (%)",
        }
    ]
