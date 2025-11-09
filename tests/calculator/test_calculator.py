from src.calculator.calculator import Calculator

def test_add():
    c = Calculator()
    assert c.add(2, 3) == 5.0

def test_factorize():
    c = Calculator()
    assert c.factorize(27) == [3, 3, 3]
