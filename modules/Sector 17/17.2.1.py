from core.change_table_module import ChangeTableModule


class CIS_17_2_1(ChangeTableModule):
    cis_id = "17.2.1"
    title = "Audit Application Group Management"
    profiles = ['dc', 'ms']

    CHANGES = [{'kind': 'auditpol', 'subcategory_guid': '{0cce9239-69ae-11d9-bed3-505054503030}', 'success': True, 'failure': True, 'label': 'Audit Application Group Management = Success and Failure'}]
