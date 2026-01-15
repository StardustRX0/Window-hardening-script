"""Example: a table-driven module.

This file lives in /examples so it WON'T be executed automatically.
When you're ready, copy it into /modules and rename it to your CIS id
(e.g. modules/Sector 2.3/2.3.1.2.py).

The main idea:
- You only edit the CHANGES list (a small "table")
- The base class handles dry-run, logging, secedit export/configure, etc.
"""

from core.change_table_module import ChangeTableModule


class Example_2_3_1_2(ChangeTableModule):
    cis_id = "2.3.1.2"
    title = "Accounts: Limit local account use of blank passwords to console logon only"

    # Applies to both profiles unless restricted.
    # You can set: profiles = ["dc"] or profiles = ["ms"]
    profiles = ["dc", "ms"]

    CHANGES = [
        {
            "kind": "secedit_registry",
            "key": r"MACHINE\System\CurrentControlSet\Control\Lsa\LimitBlankPasswordUse",
            "value": "4,1",  # 4 = REG_DWORD, 1 = enabled
            "label": "Limit blank-password use",
        }
    ]
