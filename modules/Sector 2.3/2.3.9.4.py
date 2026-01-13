from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.9.4"
    title = "Microsoft network server: Disconnect clients when logon hours expire"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\EnableForcedLogoff",
            "value": "4,1",
            "label": "Disconnect clients when logon hours expire",
        }
    ]
