from unittest import TestCase

from roman_numerals import roman_for


class TestRomanFor(TestCase):

    def test_converts(self):
        assert roman_for(1) == "I"
        assert roman_for(3) == "III"
        assert roman_for(4) == "IV"
        assert roman_for(5) == "V"
        assert roman_for(8) == "VIII"
        assert roman_for(9) == "IX"
        assert roman_for(10) == "X"
        assert roman_for(11) == "XI"
        assert roman_for(14) == "XIV"
        assert roman_for(80) == "LXXX"
        assert roman_for(294) == "CCXCIV"
        assert roman_for(2019) == "MMXIX"
