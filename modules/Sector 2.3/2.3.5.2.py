from core.change_table_module import ChangeTableModule


class CIS_2_3_5_2(ChangeTableModule):
    cis_id = "2.3.5.2"
    title = "Domain controller: Allow vulnerable Netlogon secure channel connections (Not Configured)"
    profiles = ["dc"]

    CHANGES = [
        {
            "kind": "registry_value_absent",
            "key": r"HKLM\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters",
            "value_name": "VulnerableChannelAllowList",
            "label": "DC: VulnerableChannelAllowList should be absent (Not Configured)",
        }
    ]
