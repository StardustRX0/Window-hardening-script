from core.change_table_module import ChangeTableModule


class CIS_2_3_5_3(ChangeTableModule):
    cis_id = "2.3.5.3"
    title = "Domain controller: LDAP server channel binding token requirements"
    profiles = ["dc"]

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Services\NTDS\Parameters\LdapEnforceChannelBind",
            "value": "4,2",
            "label": "DC: LDAP channel binding token requirements (Always)",
        }
    ]
