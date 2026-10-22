def number_checker(value):
    if not value.isdigit():
        raise ValueError("Not a number!")
