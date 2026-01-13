from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.9.5"
    title = "Microsoft network server: Server SPN target name validation level"
    profiles = ['ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters\SMBServerNameHardeningLevel",
            "value": "4,1",
            "label": "Server SPN target name validation level (Accept if provided by client)",
        }
    ]
