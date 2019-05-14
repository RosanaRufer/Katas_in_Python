from unittest import TestCase


def is_leap(year):
    return False


class TestIs_leap(TestCase):
    def test_is_leap(self):
        self.assertEqual(is_leap(4), True)
