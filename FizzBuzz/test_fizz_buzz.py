from fizz_buzz import fizz_buzz


def test_should_return_number_for_non_three_or_five_multiples():
    assert fizz_buzz(2) == 2


def test_should_return_fizz_for_three_multiples():
    assert fizz_buzz(3) == 'Fizz'


def test_should_return_buzz_for_five_multiples():
    assert fizz_buzz(5) == 'Buzz'


def test_should_return_fizzbuzz_for_five_multiples():
    assert fizz_buzz(15) == 'FizzBuzz'
