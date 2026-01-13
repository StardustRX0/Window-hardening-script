from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.17.5"
    title = "User Account Control: Only elevate UIAccess applications that are installed in secure locations"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\EnableSecureUIAPaths",
            "value": "4,1",
            "label": "Set EnableSecureUIAPaths=1 (Enabled)",
        },
    ]
