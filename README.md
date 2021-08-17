## FmanActionBar

Plugin for [fman.io](https://fman.io).

Add top & bottom action bars with button for various actions.

Config in `action_bar.json`

```json
{
    "top": [],
    "bottom": [
    	["<button text>", "<pane action name>"],
        ["Explorer", "open_native_file_manager"],
        ["<button text>", "app:<application action name>"],
        ["About", "app:about"],
        ["<button text>", "<action name>", "<action params>"],
        ["C:", "open", {"url": "file://c:"}]
    ]
}
```

Install with [fman's built-in command for installing plugins](https://fman.io/docs/installing-plugins).

## Preview

![image](https://user-images.githubusercontent.com/2664578/129769853-f9755cff-8b6a-44f2-9461-34f2a507e573.png)
