import pytest
from project5 import Project5


@pytest.fixture
def p():
    return Project5()


# --- single symbols ---

def test_one_encodes_to_single_symbol(p):
    assert p.encode(1) == "I"

def test_five_encodes_to_single_symbol(p):
    assert p.encode(5) == "V"

def test_ten_encodes_to_single_symbol(p):
    assert p.encode(10) == "X"

def test_fifty_encodes_to_single_symbol(p):
    assert p.encode(50) == "L"

def test_one_hundred_encodes_to_single_symbol(p):
    assert p.encode(100) == "C"

def test_five_hundred_encodes_to_single_symbol(p):
    assert p.encode(500) == "D"

def test_one_thousand_encodes_to_single_symbol(p):
    assert p.encode(1000) == "M"


# --- subtractive pairs ---

def test_four_uses_subtractive_notation(p):
    assert p.encode(4) == "IV"

def test_nine_uses_subtractive_notation(p):
    assert p.encode(9) == "IX"

def test_forty_uses_subtractive_notation(p):
    assert p.encode(40) == "XL"

def test_ninety_uses_subtractive_notation(p):
    assert p.encode(90) == "XC"

def test_four_hundred_uses_subtractive_notation(p):
    assert p.encode(400) == "CD"

def test_nine_hundred_uses_subtractive_notation(p):
    assert p.encode(900) == "CM"


# --- composite values ---

def test_repeating_symbols_are_concatenated(p):
    assert p.encode(3) == "III"

def test_value_combining_multiple_symbols(p):
    assert p.encode(58) == "LVIII"

def test_complex_value_with_subtractive_notation(p):
    assert p.encode(1994) == "MCMXCIV"
