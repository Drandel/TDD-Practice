import pytest
from project3 import Project3


@pytest.fixture
def p():
    return Project3()


# --- evaluate ---

def test_returns_number_as_string_when_no_conditions_met(p):
    assert p.evaluate(1) == "1"

def test_returns_number_as_string_for_another_plain_value(p):
    assert p.evaluate(7) == "7"

def test_divisible_by_three_returns_first_label(p):
    assert p.evaluate(3) == "Fizz"

def test_divisible_by_three_non_trivial(p):
    assert p.evaluate(9) == "Fizz"

def test_divisible_by_five_returns_second_label(p):
    assert p.evaluate(5) == "Buzz"

def test_divisible_by_five_non_trivial(p):
    assert p.evaluate(10) == "Buzz"

def test_divisible_by_both_returns_combined_label(p):
    assert p.evaluate(15) == "FizzBuzz"

def test_divisible_by_both_non_trivial(p):
    assert p.evaluate(30) == "FizzBuzz"


# --- evaluate_range ---

def test_range_returns_a_list(p):
    result = p.evaluate_range(1, 5)
    assert isinstance(result, list)

def test_range_returns_correct_number_of_elements(p):
    result = p.evaluate_range(1, 10)
    assert len(result) == 10

def test_range_first_five_values(p):
    result = p.evaluate_range(1, 5)
    assert result == ["1", "2", "Fizz", "4", "Buzz"]

def test_range_includes_combined_label_at_correct_position(p):
    result = p.evaluate_range(13, 15)
    assert result == ["13", "14", "FizzBuzz"]
