from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "5.2"
    title = "Print Spooler (Spooler) is set to Disabled (MS only)"
    profiles = ["ms"]

    CHANGES = [
        {
            "kind": "windows_service",
            "service": "Spooler",
            "startup_type": "disabled",
            "state": "stopped",
            "label": "Disable Print Spooler service",
        },
    ]
