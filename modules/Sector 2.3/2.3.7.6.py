from core.change_table_module import ChangeTableModule


class CIS_2_3_7_6(ChangeTableModule):
    cis_id = "2.3.7.6"
    title = "Interactive logon: Number of previous logons to cache (in case domain controller is not available)"
    # CIS: Member Server only
    profiles = ['ms']

    CHANGES = [
        {
            'kind': 'secedit_registry',
            # Cached logons count is stored as a REG_SZ string.
            'key': 'MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\CachedLogonsCount',
            'value': '1,"4"',
            'label': 'CachedLogonsCount = 4 (or fewer)',
        },
    ]
