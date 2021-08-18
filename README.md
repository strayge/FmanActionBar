# FmanActionBar
## Overview
Plugin for [fman.io](https://fman.io).
Adds top & bottom action bars with buttons (configurable) for various actions.

## Installation
[Ctrl+Shift+P -> Install Plugins -> FmanActionBar](https://fman.io/docs/installing-plugins)

## Usage
After installation, the top and bottom action bars will appear enabling you to click on them using he mouse as well as being nice UI guides for your common actions

## Configuration
In order to configure the action bars edit the [action_bar.json](action_bar.json) file (in the plugin folder)

### Examples for different menu items:
```json
        ["<button text>", "<pane action name>"],
        ["<button text>", "<action name>", "<action params>"],
        ["<button text>", "app:<application action name>"]
```

### Full example of configured top & down action menus
```json
{
    "top": [
        ["C:", "open", {"url": "file://c:"}],
        ["Show Properties", "show_explorer_properties"],
        ["Pack", "pack"],

        ["Commands", "command_palette"],
        ["Zen", "app:zen_of_fman"],
        ["Help", "app:help"],
        ["About", "app:about"]
],
    "bottom": [
        ["[F3] View", "view"],
        ["[F4] Edit", "open_with_editor"],
        ["[F5] Copy", "copy"],
        ["[F6] Move", "move"],
        ["[SH+F6] Rename", "rename"],
        ["[F7] New folder", "create_directory"],
        ["[F9] Terminal", "open_terminal"],
        ["[F10] Explorer", "open_native_file_manager"]
    ]
}
```

### Preview of the above example
![Showing the top and bottom action bars for the above example](https://user-images.githubusercontent.com/2664578/129769853-f9755cff-8b6a-44f2-9461-34f2a507e573.png)

### Default (Out of the box) action menu configuration
```json
{
    "top": [],
    "bottom": [
        ["[F3] View", "view"],
        ["[F4] Edit", "open_with_editor"],
        ["[F5] Copy", "copy"],
        ["[F6] Move", "move"],
        ["[SH+F6] Rename", "rename"],
        ["[F7] New folder", "create_directory"],
        ["[F9] Terminal", "open_terminal"],
        ["[F10] Explorer", "open_native_file_manager"]
    ]
}
```

### Preview of fman using the action bar with default values
![Showing the top and bottom action bars using the default values](https://user-images.githubusercontent.com/2664578/129769853-f9755cff-8b6a-44f2-9461-34f2a507e573.png)

## Disclaimer
The theme in the screenshots was changed using [Fman Alternative Colors](https://github.com/strayge/FmanAlternativeColors) plugin  
The two dots (..) are presented using [Fman Dot Entries](https://github.com/strayge/FmanDotEntries) plugin  
