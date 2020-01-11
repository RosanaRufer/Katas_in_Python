from FizzBuzz.fizz_buzz_two.fizz_buzz_two import fizz_buzz_two


def test_general_case_one():
    """
    When I fizzbuzz number 1, I get back a string representing it
    """
    assert fizz_buzz_two(1) == "1"


def test_general_case_two():
    """
    When I fizzbuzz number 2, I get back a string representing it
    """
    assert fizz_buzz_two(2) == "2"


def test_general_case_four():
    """
    When I fizzbuzz number 4, I get back a string representing it
    """
    assert fizz_buzz_two(4) == "4"


def test_divisible_by_three_one():
    """
    When I fizzbuzz number 3, I get back  "Fizz"
    """
    assert fizz_buzz_two(3) == "Fizz"


def test_divisible_by_three_two():
    """
    When I fizzbuzz number 9, I get back  "Fizz"
    """
    assert fizz_buzz_two(9) == "Fizz"


def test_divisible_by_five_one():
    """
    When I fizzbuzz number 5, I get back  "Buzz"
    """
    assert fizz_buzz_two(5) == "Buzz"
