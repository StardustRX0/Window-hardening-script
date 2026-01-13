from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.10.4"
    title = "Network access: Do not allow storage of passwords and credentials for network authentication"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\DisableDomainCreds",
            "value": "4,1",
            "label": "Do not allow storage of passwords and credentials for network authentication",
        }
    ]
