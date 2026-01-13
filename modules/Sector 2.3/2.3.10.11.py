from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.10.11"
    title = "Network access: Restrict clients allowed to make remote calls to SAM"
    profiles = ['ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\RestrictRemoteSAM",
            "value": r"1,O:BAG:BAD:(A;;RC;;;BA)",
            "label": "Set RestrictRemoteSAM to 'Administrators: Remote Access: Allow'",
        },
    ]
