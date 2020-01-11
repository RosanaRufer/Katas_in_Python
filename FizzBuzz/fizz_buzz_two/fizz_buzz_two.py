def divisible_by_3(number: int):
    return number % 3 == 0


def fizz_buzz_two(number: int):
    if divisible_by_3(number):
        return "Fizz"
    return str(number)
