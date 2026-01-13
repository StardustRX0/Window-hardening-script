from core.change_table_module import ChangeTableModule


class CIS_18_5_6(ChangeTableModule):
    """18.5.6 Ensure 'MSS: (NoNameReleaseOnDemand) Allow the computer to ignore NetBIOS name release requests except from WINS servers'."""

    cis_id = "18.5.6"
    title = "MSS (NoNameReleaseOnDemand) Ignore NetBIOS name release requests except from WINS servers"
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "reg_set",
            "key": "HKLM\\SYSTEM\\CurrentControlSet\\Services\\NetBT\\Parameters",
            "value_name": "NoNameReleaseOnDemand",
            "value_type": "REG_DWORD",
            "value": 1,
            "label": "Ignore NetBIOS name release requests (NoNameReleaseOnDemand=1)",
        },
    ]
