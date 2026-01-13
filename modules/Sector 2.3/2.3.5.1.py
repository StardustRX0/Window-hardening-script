from core.change_table_module import ChangeTableModule


class CIS_2_3_5_1(ChangeTableModule):
    cis_id = "2.3.5.1"
    title = "Domain controller: Allow server operators to schedule tasks"
    profiles = ["dc"]

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\SubmitControl",
            "value": "4,0",
            "label": "DC: Disallow server operators scheduling tasks",
        }
    ]
