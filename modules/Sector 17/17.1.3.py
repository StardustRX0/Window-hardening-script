from core.change_table_module import ChangeTableModule


class CIS_17_1_3(ChangeTableModule):
    cis_id = "17.1.3"
    title = "Audit Kerberos Service Ticket Operations"
    profiles = ['dc']

    CHANGES = [{'kind': 'auditpol', 'subcategory_guid': '{0cce9240-69ae-11d9-bed3-505054503030}', 'success': True, 'failure': True, 'label': 'Audit Kerberos Service Ticket Operations = Success and Failure'}]
