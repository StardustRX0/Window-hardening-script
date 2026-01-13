from core.change_table_module import ChangeTableModule


class CIS18_7_5(ChangeTableModule):
    """
    CIS 18.7.5: Configure RPC connection settings: Protocols to allow for incoming RPC connections
    """

    cis_id = "18.7.5"
    title = "Configure RPC connection settings: Protocols to allow for incoming RPC connections"
    profiles = ['DC', 'MS']

    CHANGES = [{'key': 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\Printers\\RPC',
  'kind': 'reg_set',
  'label': 'Allow incoming RPC over TCP only',
  'value': 5,
  'value_name': 'RpcProtocols',
  'value_type': 'DWORD'}]
