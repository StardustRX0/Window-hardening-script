from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.11.6"
    title = "Network security: Force logoff when logon hours expire (Manual)"
    profiles = ['dc', 'ms']

    CHANGES = [
    ]

    def apply(self) -> None:
        self.log_change("Manual control in CIS: verify via Group Policy UI path Computer Configuration\\Policies\\Windows Settings\\Security Settings\\Local Policies\\Security Options. Recommended state: Enabled. This tool does not enforce it automatically.")
