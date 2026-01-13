from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.11.9"
    title = "Network security: LDAP client signing requirements"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Services\LDAP\LDAPClientIntegrity",
            "value": "4,1",
            "label": "Set LDAPClientIntegrity=1 (Negotiate signing)",
        },
    ]
