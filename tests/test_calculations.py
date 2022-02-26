
import pytest
from app.calculations import add, subtract, multiply, divide

@pytest.mark.parametrize("x, y, result", [
    (3, 2, 5),
    (7, 1, 8),
    (12, 4, 16)
])


def test_add(x, y, result):
    assert add(x, y) == result

def test_subtract():
    assert subtract(9, 4) == 5

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(20, 5) == 4    