from core.change_table_module import ChangeTableModule


class CIS_2_3_4_1(ChangeTableModule):
    cis_id = "2.3.4.1"
    title = "Devices: Prevent users from installing printer drivers"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Print\Providers\LanMan Print Services\Servers\AddPrinterDrivers",
            "value": "4,1",
            "label": "Devices: Prevent users from installing printer drivers",
        }
    ]
