# open_dir

Opens a directory dialog to prompt the user for selecting a directory.

## Possible Arguments:

| Argument | Description | Type | Default |
| --- | --- | --- | --- |
| **`**dirdialogargs`** | Additional keyword arguments to be passed to the underlying directory dialog method. | `**kwargs` |  |

## Returns:

The selected directory path as a string.

## Use:
```python
from einfach import open_dir

# Example 1: Prompt user to select a directory.
dir_path = open_dir()
# Returns the selected directory path as a string.

# Example 2: Prompt user to select a directory. And specify directory dialog options.
dir_path = open_dir(title="Select a directory")
```

!!! note
    There are no `modes` for `open_dir`.