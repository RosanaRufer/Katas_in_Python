from unittest import TestCase

from Leap_Year.is_leap import is_leap


class TesIsLeap(TestCase):
    def test_is_leap(self):
        self.assertEqual(is_leap(4), True)
