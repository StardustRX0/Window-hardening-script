from core.change_table_module import ChangeTableModule


class CIS18_7_4(ChangeTableModule):
    """
    CIS 18.7.4: Configure RPC connection settings: Use authentication for outgoing RPC connections
    """

    cis_id = "18.7.4"
    title = "Configure RPC connection settings: Use authentication for outgoing RPC connections"
    profiles = ['DC', 'MS']

    CHANGES = [{'key': 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\Printers\\RPC',
  'kind': 'reg_set',
  'label': 'Enable authentication for outgoing RPC connections',
  'value': 0,
  'value_name': 'RpcAuthentication',
  'value_type': 'DWORD'}]
