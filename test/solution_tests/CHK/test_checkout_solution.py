from lib.solutions.CHK import checkout_solution
import pytest

def test_checkout_1(self):
    assert checkout_solution("AAA")==130
    assert checkout_solution("A") ==50
    
    
if __name__ == "__main__":
    pytest.main()