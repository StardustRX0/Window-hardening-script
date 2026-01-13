from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.10.10"
    title = "Network access: Restrict anonymous access to Named Pipes and Shares"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\RestrictNullSessAccess",
            "value": "4,1",
            "label": "Set RestrictNullSessAccess=1 (Enabled)",
        },
    ]
