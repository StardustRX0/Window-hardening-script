from core.change_table_module import ChangeTableModule


class CIS18_9_4_2(ChangeTableModule):
    """CIS 18.9.4.2"""

    cis_id = "18.9.4.2"
    title = "Remote host allows delegation of non-exportable credentials"
    description = 'Enables support for Restricted Admin Mode and Windows Defender Remote Credential Guard. This reduces the risk of credential theft over Remote Desktop connections.'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": 'reg_set',
            "key": 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\CredentialsDelegation',
            "value_name": 'AllowProtectedCreds',
            "value_type": 'REG_DWORD',
            "value": 1,
            "label": 'Computer Configuration\\Policies\\Administrative Templates\\System\\Credentials Delegation\\Remote host allows delegation of non-exportable credentials',
        },
    ]
