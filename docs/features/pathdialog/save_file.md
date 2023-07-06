# save_file

Opens a file dialog to prompt the user for file saving based on the specified mode.

## Possible Arguments:

| Argument              | Description                                                                   | Type                  | Default |
| --------------------- | ----------------------------------------------------------------------------- | --------------------- | ------- |
| **`mode`**            | The mode of the file dialog.                                                  | `str`                 |         |
| **`**filedialogargs`** | Additional keyword arguments to be passed to the underlying file dialog method from tkinter. | `**kwargs`            |         |

## Returns:

The selected file path for saving the file, based on the specified mode.

## Modes:

The `mode` argument can be one of the following values:

- **"file"**: Prompts the user to select a file path for saving. Returns a single file path as a string.

- **"file_name"**: Prompts the user to select a file path for saving, including specifying the file name. Returns a single file path as a string.

## Use:
```python
from einfach import save_file

# Example 1: Prompt user to select a file for saving.
file_path = save_file(mode="file")
# Returns the selected file path as a string.

# Example 2: Prompt user to select a file for saving. And specify file dialog options.
file_path = save_file(mode="file_name", title="Save a file", defaultextension=".txt")
# Returns the selected file path as a string
```

!!! note
    There is no "files" or "file_names" mode for saving files