from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.10.2"
    title = "Network access: Do not allow anonymous enumeration of SAM accounts"
    profiles = ['ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\RestrictAnonymousSAM",
            "value": "4,1",
            "label": "Do not allow anonymous enumeration of SAM accounts",
        }
    ]
