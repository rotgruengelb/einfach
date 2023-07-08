# would_be_valid_float

Checks if a given string value can be converted to a valid float.

## Possible Arguments:

| Argument | Description | Type | Default |
| --- | --- | --- | --- |
| **`value`** | The string value to be checked. | `str` |  |

## Returns:

A boolean value indicating whether the `value` can be converted to a valid float. Returns `True` if the `value` can be converted to a float, and `False` otherwise.

## Use:
```python
from einfach import would_be_valid_float

result = would_be_valid_float(value="3.14")
# Returns True, as the string "3.14" can be converted to a valid float.

result = would_be_valid_float(value="Hello")
# Returns False, as the string "Hello" cannot be converted to a valid float.

result = would_be_valid_float(value="123")
# Returns True, as the string "123" can be converted to a valid float.
```