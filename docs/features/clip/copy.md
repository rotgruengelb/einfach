# copy

Copies a string into the user's clipboard 

!!! warning "Compatibility"

    This currently only works on the `win32` (Windows OS) platform.

## Possible Arguments:

|Argument|Description|Type|Default|
|--| ---------------------------------------------------------------------------|--|--|
|**`content`** | The String that should be put in the users clipboard. _This string cannot be empty or only contain whitespace/spaces_| `str` | |
|`no_os_error`|Tells the function to not raise a `OSError` when the operating system is not `win32`| `bool` |`False`|

## Use:
```py
from einfach import clip

clip.copy(content="Hello World") 
# This will copy 'Hello World' into the users clipboard (if on win32).
# This wont ignore the OSError that is raised when not run on win32.
    
clip.copy(content="Hi! :D", no_os_error=True) 
# This will ignore the OSError if run on a non win32 platform. 
# Note: This will result in the clipboard not changing on the non-win32 system. 
```