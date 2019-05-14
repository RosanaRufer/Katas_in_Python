def fizz_buzz(number):
    three_multiple = number % 3 == 0
    five_multiple = number % 5 == 0

    if three_multiple and five_multiple:
        return 'FizzBuzz'
    elif three_multiple:
        return 'Fizz'
    elif five_multiple:
        return 'Buzz'
    else:
        return number
