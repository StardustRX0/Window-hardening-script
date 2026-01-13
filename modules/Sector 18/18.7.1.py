from core.change_table_module import ChangeTableModule


class CIS18_7_1(ChangeTableModule):
    """
    CIS 18.7.1: Allow Print Spooler to accept client connections
    """

    cis_id = "18.7.1"
    title = "Allow Print Spooler to accept client connections"
    profiles = ['DC', 'MS']

    CHANGES = [{'key': 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\Printers',
  'kind': 'reg_set',
  'label': 'Disable Print Spooler accepting client connections (requires spooler restart)',
  'value': 2,
  'value_name': 'RegisterSpoolerRemoteRpcEndPoint',
  'value_type': 'DWORD'}]
