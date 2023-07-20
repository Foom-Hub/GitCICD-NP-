import calculator
import pytest

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtract():
    assert calculator.subtract(2, 3) == -1
    assert calculator.subtract(-1, 1) == -2
    assert calculator.subtract(0, 0) == 0

def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-1, 1) == -1
    assert calculator.multiply(0, 0) == 0

def test_divide():
    assert calculator.divide(6, 3) == 2.0
    assert calculator.divide(-1, 1) == -1.0
    assert calculator.divide(5, 2) == pytest.approx(2.5)
    with pytest.raises(Exception):
        calculator.divide(5, 0)