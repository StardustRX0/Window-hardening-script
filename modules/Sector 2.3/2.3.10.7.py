from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.10.7"
    title = "Network access: Named Pipes that can be accessed anonymously"
    profiles = ['ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\NullSessionPipes",
            "value": "7,",
            "label": "Named Pipes that can be accessed anonymously (MS null value)",
        }
    ]
