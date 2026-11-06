def is_number(value) -> bool:
    if not value.isdigit():
        return False
    return True


def is_float(value) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False
