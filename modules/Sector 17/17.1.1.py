from core.change_table_module import ChangeTableModule


class CIS_17_1_1(ChangeTableModule):
    cis_id = "17.1.1"
    title = "Audit Credential Validation"
    profiles = ['dc', 'ms']

    CHANGES = [{'kind': 'auditpol', 'subcategory_guid': '{0cce923f-69ae-11d9-bed3-505054503030}', 'success': True, 'failure': True, 'label': 'Audit Credential Validation = Success and Failure'}]
