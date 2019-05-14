def is_leap(year):
    if is_divisible(year, 100) and not is_divisible(year, 400):
        return False
    return is_divisible(year, 4)


def is_divisible(dividend, divisor):
    return dividend % divisor == 0
