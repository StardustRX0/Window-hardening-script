from core.change_table_module import ChangeTableModule


class CIS18_6_20_1(ChangeTableModule):
    """CIS 18.6.20.1 (L2)

    Ensure 'Configuration of wireless settings using Windows Connect Now' is set to 'Disabled'.
    """

    cis_id = "18.6.20.1"
    title = "Configuration of wireless settings using Windows Connect Now"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\WCN\Registrars",
            "value_name": "DisableFlashConfigRegistrar",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "WCN Registrars: DisableFlashConfigRegistrar",
        },
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\WCN\Registrars",
            "value_name": "DisableInBand802DOT11Registrar",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "WCN Registrars: DisableInBand802DOT11Registrar",
        },
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\WCN\Registrars",
            "value_name": "DisableUPnPRegistrar",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "WCN Registrars: DisableUPnPRegistrar",
        },
        {
            "kind": "reg_set",
            "key": r"HKLM\SOFTWARE\Policies\Microsoft\Windows\WCN\Registrars",
            "value_name": "DisableWPDRegistrar",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "WCN Registrars: DisableWPDRegistrar",
        },
    ]
