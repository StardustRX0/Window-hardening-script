from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.11.8"
    title = "Network security: LDAP client encryption requirements"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Services\LDAP\LDAPClientConfidentiality",
            "value": "4,1",
            "label": "Set LDAPClientConfidentiality=1 (Negotiate sealing)",
        },
    ]
