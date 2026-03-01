import pytest
from project1 import Project1


@pytest.fixture
def p():
    return Project1()


# --- add ---

def test_add_two_positive_numbers(p):
    assert p.add(2, 3) == 5

def test_add_two_negative_numbers(p):
    assert p.add(-4, -6) == -10

def test_add_positive_and_negative(p):
    assert p.add(10, -3) == 7

def test_add_with_zero(p):
    assert p.add(0, 5) == 5

def test_add_two_zeros(p):
    assert p.add(0, 0) == 0


# --- subtract ---

def test_subtract_two_positive_numbers(p):
    assert p.subtract(10, 4) == 6

def test_subtract_results_in_negative(p):
    assert p.subtract(3, 9) == -6

def test_subtract_negative_from_positive(p):
    assert p.subtract(5, -2) == 7

def test_subtract_with_zero(p):
    assert p.subtract(7, 0) == 7


# --- multiply ---

def test_multiply_two_positive_numbers(p):
    assert p.multiply(3, 4) == 12

def test_multiply_by_zero(p):
    assert p.multiply(99, 0) == 0

def test_multiply_two_negative_numbers(p):
    assert p.multiply(-3, -4) == 12

def test_multiply_positive_and_negative(p):
    assert p.multiply(5, -3) == -15

def test_multiply_by_one(p):
    assert p.multiply(7, 1) == 7


# --- divide ---

def test_divide_two_positive_numbers(p):
    assert p.divide(10, 2) == 5

def test_divide_results_in_float(p):
    assert p.divide(7, 2) == 3.5

def test_divide_negative_by_positive(p):
    assert p.divide(-9, 3) == -3

def test_divide_number_by_itself(p):
    assert p.divide(8, 8) == 1

def test_divide_by_zero_raises_error(p):
    with pytest.raises(ValueError):
        p.divide(10, 0)
