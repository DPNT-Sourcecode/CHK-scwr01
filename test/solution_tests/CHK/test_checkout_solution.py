from lib.solutions.CHK.checkout_solution import checkout
import pytest

def test_checkout_1():
    """test_checkout_1 1 round
    """
    assert checkout("AAA")==130
    assert checkout("A") ==50
    assert checkout("AA") == 100
    
def test_checkout_2():
    """ test_checkout 2 round
    """
    
    
    
if __name__ == "__main__":
    pytest.main()