from core.change_table_module import ChangeTableModule


class CIS18_9_7_2(ChangeTableModule):
    """CIS 18.9.7.2"""

    cis_id = "18.9.7.2"
    title = "Prevent device metadata retrieval from the Internet"
    description = 'Prevents Windows from retrieving device metadata (and related third-party utilities) from the Internet.'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": 'reg_set',
            "key": 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Device Metadata',
            "value_name": 'PreventDeviceMetadataFromNetwork',
            "value_type": 'REG_DWORD',
            "value": 1,
            "label": 'Computer Configuration\\Policies\\Administrative Templates\\System\\Device Installation\\Prevent device metadata retrieval from the Internet',
        },
    ]
