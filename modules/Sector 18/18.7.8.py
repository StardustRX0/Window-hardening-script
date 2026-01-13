from core.change_table_module import ChangeTableModule


class CIS18_7_8(ChangeTableModule):
    """
    CIS 18.7.8: Configure RPC packet level privacy setting for incoming connections
    """

    cis_id = "18.7.8"
    title = "Configure RPC packet level privacy setting for incoming connections"
    profiles = ['DC', 'MS']

    CHANGES = [{'key': 'HKLM\\SYSTEM\\CurrentControlSet\\Control\\Print',
  'kind': 'reg_set',
  'label': 'Enable RPC packet level privacy for incoming print connections',
  'value': 1,
  'value_name': 'RpcAuthnLevelPrivacyEnabled',
  'value_type': 'DWORD'}]
