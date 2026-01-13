from core.change_table_module import ChangeTableModule


class CIS18_7_3(ChangeTableModule):
    """
    CIS 18.7.3: Configure RPC connection settings: Protocol to use for outgoing RPC connections
    """

    cis_id = "18.7.3"
    title = "Configure RPC connection settings: Protocol to use for outgoing RPC connections"
    profiles = ['DC', 'MS']

    CHANGES = [{'key': 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\Printers\\RPC',
  'kind': 'reg_set',
  'label': 'Set outgoing RPC protocol to RPC over TCP',
  'value': 0,
  'value_name': 'RpcUseNamedPipeProtocol',
  'value_type': 'DWORD'}]
