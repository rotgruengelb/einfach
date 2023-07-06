# is_float_in_range

Checks if a given float or integer value is within a specified range.

## Possible Arguments:

| Argument   | Description                                                  | Type                 | Default |
| ---------- | ------------------------------------------------------------ | -------------------- | ------- |
| **`value`** | The value to be checked.                                     | `float` or `int`     |         |
| **`min_value`** | The minimum value of the range.                             | `float` or `int`     |         |
| **`max_value`** | The maximum value of the range.                             | `float` or `int`     |         |

## Returns:

A boolean value indicating whether the `value` is within the specified range (`min_value` to `max_value`). Returns `True` if the `value` is within the range, and `False` otherwise.

## Use:
```python
from einfach import is_float_in_range

result = is_float_in_range(value=3.5, min_value=2.0, max_value=5.0)
# Returns True, as 3.5 is within the range of 2.0 and 5.0.

result = is_float_in_range(value=7.2, min_value=1, max_value=6)
# Returns False, as 7.2 is not within the range of 1 and 6.

result = is_float_in_range(value=10, min_value=5, max_value=15)
# Returns True, as 10 is within the range of 5 and 15.
```