from roman_numerals import roman_for


def test_converts_one():
    assert roman_for(1) == "I"


def test_converts_three():
    assert roman_for(3) == "III"


def test_converts_four():
    assert roman_for(4) == "IV"


def test_converts_five():
    assert roman_for(5) == "V"


def test_converts_six():
    assert roman_for(6) == "VI"


def test_converts_eight():
    assert roman_for(8) == "VIII"


def test_converts_nine():
    assert roman_for(9) == "IX"


def test_converts_ten():
    assert roman_for(10) == "X"


def test_converts_thirteen():
    assert roman_for(13) == "XIII"


def test_converts_forty():
    assert roman_for(40) == "XL"




