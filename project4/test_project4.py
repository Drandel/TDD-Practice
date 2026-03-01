import pytest
from project4 import Project4


@pytest.fixture
def p():
    return Project4()


# --- basic inputs ---

def test_empty_string_returns_zero(p):
    assert p.add("") == 0

def test_single_number_returns_its_value(p):
    assert p.add("1") == 1

def test_two_numbers_comma_separated_returns_sum(p):
    assert p.add("1,2") == 3

def test_multiple_numbers_returns_sum(p):
    assert p.add("1,2,3,4") == 10


# --- newline as delimiter ---

def test_newline_is_a_valid_delimiter(p):
    assert p.add("1\n2,3") == 6

def test_newlines_and_commas_can_be_mixed(p):
    assert p.add("1\n2\n3") == 6


# --- custom delimiter ---

def test_custom_delimiter_defined_in_header(p):
    assert p.add("//;\n1;2") == 3

def test_custom_delimiter_can_be_any_character(p):
    assert p.add("//|\n3|4|5") == 12


# --- negative numbers ---

def test_single_negative_raises_error(p):
    with pytest.raises(ValueError):
        p.add("-1,2")

def test_exception_message_contains_the_negative_number(p):
    with pytest.raises(ValueError) as exc_info:
        p.add("1,-1,2")
    assert "-1" in str(exc_info.value)

def test_all_negatives_listed_in_exception_message(p):
    with pytest.raises(ValueError) as exc_info:
        p.add("-1,2,-3")
    message = str(exc_info.value)
    assert "-1" in message
    assert "-3" in message


# --- numbers greater than 1000 ---

def test_numbers_greater_than_1000_are_ignored(p):
    assert p.add("2,1001") == 2

def test_exactly_1000_is_not_ignored(p):
    assert p.add("1000,1") == 1001
