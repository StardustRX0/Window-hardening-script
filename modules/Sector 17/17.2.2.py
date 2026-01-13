from core.change_table_module import ChangeTableModule


class CIS_17_2_2(ChangeTableModule):
    cis_id = "17.2.2"
    title = "Audit Computer Account Management"
    profiles = ['dc', 'ms']

    CHANGES = [{'kind': 'auditpol', 'subcategory_guid': '{0cce9236-69ae-11d9-bed3-505054503030}', 'success': True, 'failure': False, 'label': 'Audit Computer Account Management = Success'}]
