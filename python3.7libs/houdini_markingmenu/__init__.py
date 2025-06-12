
"""Utility helpers for launching the marking menu."""

import hou

from .python import markingmenu


def show_menu(editor=None):
    """Display the marking menu in the given network editor.

    When ``editor`` is ``None``, the network editor under the cursor is used.
    The menu honours the current keyboard modifiers so the Control and Shift
    variants defined in ``menu_prefs.json`` can be triggered via hotkeys.
    """

    if editor is None:
        editor = hou.ui.paneTabUnderCursor()

    if isinstance(editor, hou.NetworkEditor):
        markingmenu.NEMarkingMenu(editor)
    else:
        raise hou.Error("No network editor found to display the marking menu")
