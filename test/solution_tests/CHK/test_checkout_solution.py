from lib.solutions.CHK import checkout_solution
import pytest

class TestCheckout():
    def test_checkout_1(self):
        assert checkout_solution("A")==50