# houdini_markingmenu
## Marking Menu for the Houdini network editor. Fast access to node creation, placement, toolscripts, and shelf tools

![Image of the Menu and Editor](/python3.7libs/houdini_markingmenu/docs/mm_screenshot.jpg?raw=true)
https://vimeo.com/251253577 (a little outdated, sorry)

## Installation
1. Copy the `python3.7libs/houdini_markingmenu` directory into
   `$HOUDINI_USER_PREF_DIR/python3.7libs` so that Houdini can import the
   package.  The menu now discovers its resources relative to this module and
   no custom environment variables are required.
2. (Optional) If you prefer using Houdini's package system, copy
   `houdini_markingmenu.json` to `$HOUDINI_USER_PREF_DIR/packages` and edit the
   `path/to/root` entry to point to the root folder of this repository.

## Hotkey command
The menu can be launched with the following Python snippet:

```python
import houdini_markingmenu
houdini_markingmenu.show_menu()
```

Assign this command to a hotkey inside a network editor. Holding **Ctrl** or
**Shift** when triggering the hotkey will display the menu variant associated
with that modifier.



