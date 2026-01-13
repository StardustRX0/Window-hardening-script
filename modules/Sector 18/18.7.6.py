from core.change_table_module import ChangeTableModule


class CIS18_7_6(ChangeTableModule):
    """
    CIS 18.7.6: Configure RPC listener settings: Authentication protocol to use for incoming RPC connections
    """

    cis_id = "18.7.6"
    title = "Configure RPC listener settings: Authentication protocol to use for incoming RPC connections"
    profiles = ['DC', 'MS']

    CHANGES = [{'key': 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\Printers\\RPC',
  'kind': 'reg_set',
  'label': 'Set incoming RPC auth protocol to Negotiate (0) or higher',
  'value': 0,
  'value_name': 'ForceKerberosForRpc',
  'value_type': 'DWORD'}]
