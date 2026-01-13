from core.change_table_module import ChangeTableModule


class CIS_18_4_3(ChangeTableModule):
    """18.4.3 Ensure 'Configure SMB v1 server'."""

    cis_id = "18.4.3"
    title = "Configure SMB v1 server"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "reg_set",
            "key": "HKLM\\SYSTEM\\CurrentControlSet\\Services\\LanmanServer\\Parameters",
            "value_name": "SMB1",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "Disable SMBv1 server (LanmanServer SMB1=0)",
        },
    ]
