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
