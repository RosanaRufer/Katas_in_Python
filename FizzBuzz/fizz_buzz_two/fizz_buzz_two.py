def divisible_by_3(number: int):
    return number % 3 == 0


def divisible_by_5(number: int):
    return number % 5 == 0


def fizz_buzz_two(number: int):
    if divisible_by_3(number) and divisible_by_5(number):
        return "FizzBuzz"
    if divisible_by_3(number):
        return "Fizz"
    if divisible_by_5(number):
        return "Buzz"
    return str(number)
