from core.change_table_module import ChangeTableModule


class CIS_18_4_7(ChangeTableModule):
    """18.4.7 Ensure 'WDigest Authentication'."""

    cis_id = "18.4.7"
    title = "WDigest Authentication"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "reg_set",
            "key": "HKLM\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\WDigest",
            "value_name": "UseLogonCredential",
            "value_type": "REG_DWORD",
            "value": 0,
            "label": "Disable WDigest plaintext credential storage (UseLogonCredential=0)",
        },
    ]
