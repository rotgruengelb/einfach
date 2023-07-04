def would_be_valid_float(value: str) -> bool:
    return str(value).replace('.', '', 1).isdigit()


def is_float_in_range(value: float or int,
                      min_value: float or int,
                      max_value: float or int) -> bool:
    return float(min_value) <= float(value) <= float(max_value)
