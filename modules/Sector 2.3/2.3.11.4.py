from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.11.4"
    title = "Network security: Configure encryption types allowed for Kerberos"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\Kerberos\Parameters\SupportedEncryptionTypes",
            "value": "4,2147483640",
            "label": "Set SupportedEncryptionTypes=2147483640",
        },
    ]
