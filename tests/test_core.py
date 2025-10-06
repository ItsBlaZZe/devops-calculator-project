import math
import pytest
from calculator.core import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 2) == 3

def test_mul():
    assert mul(4, 3) == 12

def test_div():
    assert div(8, 2) == 4

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)

def test_floats():
    assert math.isclose(add(0.1, 0.2), 0.3, rel_tol=1e-9, abs_tol=1e-12)
