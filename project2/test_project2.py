import pytest
from project2 import Project2


@pytest.fixture
def p():
    return Project2()


# --- get_total ---

def test_initial_total_is_zero(p):
    assert p.get_total() == 0

def test_add_single_item_reflects_in_total(p):
    p.add_item("apple", 1.50)
    assert p.get_total() == 1.50

def test_add_multiple_items_sums_correctly(p):
    p.add_item("apple", 1.50)
    p.add_item("bread", 2.00)
    p.add_item("milk", 0.99)
    assert p.get_total() == pytest.approx(4.49)

def test_add_item_with_quantity(p):
    p.add_item("apple", 1.50, quantity=3)
    assert p.get_total() == pytest.approx(4.50)

def test_add_same_item_twice_accumulates_quantity(p):
    p.add_item("apple", 1.50, quantity=2)
    p.add_item("apple", 1.50, quantity=3)
    assert p.get_total() == pytest.approx(7.50)


# --- get_item_count ---

def test_initial_item_count_is_zero(p):
    assert p.get_item_count() == 0

def test_item_count_reflects_unique_items(p):
    p.add_item("apple", 1.50)
    p.add_item("bread", 2.00)
    assert p.get_item_count() == 2

def test_adding_same_item_does_not_increase_unique_count(p):
    p.add_item("apple", 1.50, quantity=2)
    p.add_item("apple", 1.50, quantity=1)
    assert p.get_item_count() == 1


# --- remove_item ---

def test_remove_item_updates_total(p):
    p.add_item("apple", 1.50)
    p.add_item("bread", 2.00)
    p.remove_item("apple")
    assert p.get_total() == pytest.approx(2.00)

def test_remove_item_updates_item_count(p):
    p.add_item("apple", 1.50)
    p.add_item("bread", 2.00)
    p.remove_item("bread")
    assert p.get_item_count() == 1

def test_remove_item_not_in_order_raises_error(p):
    p.add_item("apple", 1.50)
    with pytest.raises(KeyError):
        p.remove_item("bread")


# --- apply_discount ---

def test_apply_discount_reduces_total(p):
    p.add_item("apple", 10.00)
    p.apply_discount(10)
    assert p.get_total() == pytest.approx(9.00)

def test_apply_discount_over_100_raises_error(p):
    p.add_item("apple", 10.00)
    with pytest.raises(ValueError):
        p.apply_discount(110)
