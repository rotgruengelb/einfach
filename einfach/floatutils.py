def would_be_valid_float(value: str) -> bool:
    return True if str(value).replace('.', '', 1).isdigit() else False


def is_float_in_range(value: float | int, 
                      min_value: float | int,
                      max_value: float | int) -> bool:
    return float(min_value) <= float(value) <= float(max_value)
