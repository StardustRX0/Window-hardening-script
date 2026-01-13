from core.change_table_module import ChangeTableModule


class CIS_2_3_7_7(ChangeTableModule):
    cis_id = "2.3.7.7"
    title = "Interactive logon: Prompt user to change password before expiration"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            'kind': 'secedit_registry',
            'key': 'MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\PasswordExpiryWarning',
            # CIS: between 5 and 14 days. We set to 5 (default) to stay compliant with minimal user impact.
            'value': '4,5',
            'label': 'PasswordExpiryWarning = 5 (days)',
        },
    ]
