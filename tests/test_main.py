"""
Test the main module.
Author: Jordan Wallschlaeger
"""
from unittest import TestCase
from main import is_div7, is_div7_str


class Test(TestCase):
    def test_is_odd(self):
        assert is_div7(0)
        assert is_div7(1)
        assert not is_div7(7)

    def test_is_odd_str(self):
        assert is_div7_str("0") == "0 is not divisible by 7."
        assert is_div7_str("1") == "1 is not divisible by 7."
        assert is_div7_str("7") == "7 is divisible by 7."
        assert is_div7_str("-1") == "Please enter a number."
        assert is_div7_str("A") == "Please enter a number."
        assert is_div7_str("") == "Please enter a number."
