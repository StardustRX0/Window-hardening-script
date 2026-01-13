from core.change_table_module import ChangeTableModule


class CIS18_9_4_1(ChangeTableModule):
    """CIS 18.9.4.1"""

    cis_id = "18.9.4.1"
    title = "Encryption Oracle Remediation (Force Updated Clients)"
    description = "Sets CredSSP Encryption Oracle Remediation to 'Force Updated Clients'. This helps block downgrade attacks against unpatched CredSSP clients."
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": 'reg_set',
            "key": 'HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\CredSSP\\Parameters',
            "value_name": 'AllowEncryptionOracle',
            "value_type": 'REG_DWORD',
            "value": 0,
            "label": 'Computer Configuration\\Policies\\Administrative Templates\\System\\Credentials Delegation\\Encryption Oracle Remediation',
        },
    ]
