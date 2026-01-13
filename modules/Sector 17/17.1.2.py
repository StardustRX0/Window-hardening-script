from core.change_table_module import ChangeTableModule


class CIS_17_1_2(ChangeTableModule):
    cis_id = "17.1.2"
    title = "Audit Kerberos Authentication Service"
    profiles = ['dc']

    CHANGES = [{'kind': 'auditpol', 'subcategory_guid': '{0cce9242-69ae-11d9-bed3-505054503030}', 'success': True, 'failure': True, 'label': 'Audit Kerberos Authentication Service = Success and Failure'}]
