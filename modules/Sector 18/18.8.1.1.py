from core.change_table_module import ChangeTableModule


class CIS18_8_1_1(ChangeTableModule):
    """CIS 18.8.1.1"""

    cis_id = "18.8.1.1"
    title = "Turn off notifications network usage"
    description = 'Disables notification network usage. This reduces unexpected network traffic and potential information leakage via cloud-based notifications.'
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": 'reg_set',
            "key": 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications',
            "value_name": 'NoCloudApplicationNotification',
            "value_type": 'REG_DWORD',
            "value": 1,
            "label": 'Computer Configuration\\Policies\\Administrative Templates\\Start Menu and Taskbar\\Notifications: Turn off notifications network usage',
        },
    ]
