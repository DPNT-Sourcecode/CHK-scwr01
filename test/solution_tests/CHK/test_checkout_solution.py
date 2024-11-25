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
    assert checkout("EEB")==80
    assert checkout("EEBB")==110
    assert checkout(123)==-1
    assert checkout("EEBC")==100
    assert checkout("EEBG")==-1
    
def test_checkout_3():
    """test_checkout_3 _summary_
    """
    assert checkout("FFF")==20
    assert checkout("FFFF")==30
    assert checkout("FFFFF")==40
    assert checkout("FFFFFF")==40
    
def test_checkout_4():
    """test_checkout_4 _summary_
    """
    assert checkout("QQQ")==80
    assert checkout("NNNM")==120
    assert checkout("QQQ")==80
    
def test_checkout_5():
    assert checkout("SSS")==45
    
if __name__ == "__main__":
    pytest.main()