# open_file

Opens a file dialog to prompt the user for file selection based on the specified mode.

## Possible Arguments:

| Argument              | Description                                                                   | Type                  | Default |
| --------------------- | ----------------------------------------------------------------------------- | --------------------- | ------- |
| **`mode`**            | The mode of the file dialog.                                                  | `str`                 |         |
| **`**filedialogargs`** | Additional keyword arguments to be passed to the underlying file dialog method from tkinter. | `**kwargs`            |         |

## Returns:

The file path(s) selected by the user, based on the specified mode.

## Modes:
The `mode` argument can be one of the following values:

- **"file"**: Prompts the user to select a single file. Returns the selected file path as a string.

- **"file_name"**: Prompts the user to select a single file, including specifying the file name. Returns the selected file path as a string.

- **"files"**: Prompts the user to select multiple files. Returns a list of selected file paths.

- **"file_names"**: Prompts the user to select multiple files, including specifying file names. Returns a list of selected file paths.

## Use:
```python
from einfach import open_file

# Example 1: Prompt user to select a single file.
file_path = open_file(mode="file")
# Returns the selected file path as a string.

# Example 2: Prompt user to select a single file. And specify file dialog options.
file_path = open_file(mode="file_name", title="Select a file", defaultextension=".txt")
# Returns the selected file path as a string.

# Example 3: Prompt user to select multiple files.
file_paths = open_file(mode="files")
# Returns a list of selected file paths.
```