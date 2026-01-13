from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.10.3"
    title = "Network access: Do not allow anonymous enumeration of SAM accounts and shares"
    profiles = ['ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\RestrictAnonymous",
            "value": "4,1",
            "label": "Do not allow anonymous enumeration of SAM accounts and shares",
        }
    ]
