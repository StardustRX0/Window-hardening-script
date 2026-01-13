from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.11.1"
    title = "Network security: Allow Local System to use computer identity for NTLM"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\UseMachineId",
            "value": "4,1",
            "label": "Set UseMachineId=1 (Enabled)",
        },
    ]
