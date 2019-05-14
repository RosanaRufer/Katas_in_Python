from unittest import TestCase

from Leap_Year.is_leap import is_leap


class TesIsLeap(TestCase):

    def test_is_leap(self):
        should_be_leap = [4, 1996, 1600]
        for number in should_be_leap:
            self.assertEqual(is_leap(number), True)

    def test_is_not_leap(self):
        should_not_be_leap = [5, 500, 1997, 1800]
        for number in should_not_be_leap:
            self.assertEqual(is_leap(number), False)
