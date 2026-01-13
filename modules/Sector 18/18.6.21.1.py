from core.change_table_module import ChangeTableModule


class CIS18_6_21_1(ChangeTableModule):
    """
    CIS 18.6.21.1: Minimize the number of simultaneous connections to the Internet or a Windows Domain
    """

    cis_id = "18.6.21.1"
    title = "Minimize the number of simultaneous connections to the Internet or a Windows Domain"
    profiles = ['DC', 'MS']

    CHANGES = [{'key': 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\WcmSvc\\GroupPolicy',
  'kind': 'reg_set',
  'label': 'Set WCM Minimize connections to 3 (Prevent Wi-Fi when on Ethernet)',
  'value': 3,
  'value_name': 'fMinimizeConnections',
  'value_type': 'DWORD'}]
