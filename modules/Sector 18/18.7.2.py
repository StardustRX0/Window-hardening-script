from core.change_table_module import ChangeTableModule


class CIS18_7_2(ChangeTableModule):
    """
    CIS 18.7.2: Configure Redirection Guard
    """

    cis_id = "18.7.2"
    title = "Configure Redirection Guard"
    profiles = ['DC', 'MS']

    CHANGES = [{'key': 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\Printers',
  'kind': 'reg_set',
  'label': 'Enable Redirection Guard',
  'value': 1,
  'value_name': 'RedirectionguardPolicy',
  'value_type': 'DWORD'}]
