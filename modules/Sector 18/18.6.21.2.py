from core.change_table_module import ChangeTableModule


class CIS18_6_21_2(ChangeTableModule):
    """
    CIS 18.6.21.2: Prohibit connection to non-domain networks when connected to domain authenticated network
    """

    cis_id = "18.6.21.2"
    title = "Prohibit connection to non-domain networks when connected to domain authenticated network"
    profiles = ['MS']

    CHANGES = [{'key': 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\WcmSvc\\GroupPolicy',
  'kind': 'reg_set',
  'label': 'Enable Prohibit connection to non-domain networks (block non-domain)',
  'value': 1,
  'value_name': 'fBlockNonDomain',
  'value_type': 'DWORD'}]
