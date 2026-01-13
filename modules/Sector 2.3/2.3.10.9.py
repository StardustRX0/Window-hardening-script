from core.change_table_module import ChangeTableModule


class Module(ChangeTableModule):
    cis_id = "2.3.10.9"
    title = "Network access: Remotely accessible registry paths and sub-paths"
    profiles = ['dc', 'ms']

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\SecurePipeServers\Winreg\AllowedPaths\Machine",
            "value": (
                r"7,"
                r"System\CurrentControlSet\Control\Print\Printers,"
                r"System\CurrentControlSet\Services\Eventlog,"
                r"Software\Microsoft\OLAP Server,"
                r"Software\Microsoft\Windows NT\CurrentVersion\Print,"
                r"Software\Microsoft\Windows NT\CurrentVersion\Windows,"
                r"System\CurrentControlSet\Control\ContentIndex,"
                r"System\CurrentControlSet\Control\Terminal Server,"
                r"System\CurrentControlSet\Control\Terminal Server\UserConfig,"
                r"System\CurrentControlSet\Control\Terminal Server\DefaultUserConfiguration,"
                r"Software\Microsoft\Windows NT\CurrentVersion\Perflib,"
                r"System\CurrentControlSet\Services\SysmonLog,"
                r"System\CurrentControlSet\Services\CertSvc,"
                r"System\CurrentControlSet\Services\WINS"
            ),
            "label": "Set AllowedPaths:Machine to CIS-recommended list",
        },
    ]
