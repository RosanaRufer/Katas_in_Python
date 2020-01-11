from FizzBuzz.fizz_buzz_two.fizz_buzz_two import fizz_buzz_two


def test_general_case():
    """
    When I fizzbuzz number 1, I get back a string representing it
    """
    assert fizz_buzz_two(1) == "1"
