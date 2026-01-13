from core.change_table_module import ChangeTableModule


class CIS18_7_7(ChangeTableModule):
    """
    CIS 18.7.7: Configure RPC over TCP port
    """

    cis_id = "18.7.7"
    title = "Configure RPC over TCP port"
    profiles = ['DC', 'MS']

    CHANGES = [{'key': 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\Printers\\RPC',
  'kind': 'reg_set',
  'label': 'Set RPC over TCP port to 0 (dynamic)',
  'value': 0,
  'value_name': 'RpcTcpPort',
  'value_type': 'DWORD'}]
