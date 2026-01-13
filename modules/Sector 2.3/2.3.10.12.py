from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.10.12"
    title = "Network access: Shares that can be accessed anonymously"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\NullSessionShares",
            "value": "7,",
            "label": "Set NullSessionShares to blank (None)",
        },
    ]
