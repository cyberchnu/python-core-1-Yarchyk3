def int_within_bounds(number, lower_bound, upper_bound):
    if isinstance(number, int):
        return lower_bound <= number < upper_bound
    else:
        return False