def divisible_by_3(number: int):
    return number % 3 == 0


def divisible_by_5(number: int):
    return number % 5 == 0


def fizz_buzz_two(number: int):
    is_divisible_by_3 = divisible_by_3(number)
    is_divisible_by_5 = divisible_by_5(number)

    if is_divisible_by_3 and is_divisible_by_5:
        return "FizzBuzz"
    if is_divisible_by_3:
        return "Fizz"
    if is_divisible_by_5:
        return "Buzz"
    return str(number)
