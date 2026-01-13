from core.change_table_module import ChangeTableModule


class CIS_2_3_5_4(ChangeTableModule):
    cis_id = "2.3.5.4"
    title = "Domain controller: LDAP server signing requirements"
    profiles = ["dc"]

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Services\NTDS\Parameters\LDAPServerIntegrity",
            "value": "4,2",
            "label": "DC: LDAP signing requirements (Require signing)",
        }
    ]
