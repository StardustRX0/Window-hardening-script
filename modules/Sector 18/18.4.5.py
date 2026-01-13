from core.change_table_module import ChangeTableModule


class CIS_18_4_5(ChangeTableModule):
    """18.4.5 Ensure 'Enable Structured Exception Handling Overwrite Protection (SEHOP)'."""

    cis_id = "18.4.5"
    title = "Enable Structured Exception Handling Overwrite Protection (SEHOP)"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "reg_set",
            "key": "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\kernel",
            "value_name": "DisableExceptionChainValidation",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "Enable SEHOP (DisableExceptionChainValidation=0)",
        },
    ]
