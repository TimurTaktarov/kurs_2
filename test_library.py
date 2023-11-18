from decimal import Decimal

from library import cm_to_inches


def test_cm_to_inches_first_num():
    digit = -2
    result = cm_to_inches(digit)
    assert result == Decimal("-0.79")
    assert type(result) == Decimal


def test_cm_to_inches_second_num():
    digit = 0.03
    result = cm_to_inches(digit)
    assert result == Decimal("0.01")
    assert type(result) == Decimal















def test_cm_to_inches_third_num():
    digit = 10
    result = cm_to_inches(digit)
    assert result == Decimal("3.94")
    assert type(result) == Decimal


def test_cm_to_inches_fourth_num():
    digit = 35.6
    result = cm_to_inches(digit)
    assert result == Decimal("14.02")
    assert type(result) == Decimal


def test_cm_to_inches_fifth_num():
    digit = 0
    result = cm_to_inches(digit)
    assert result == Decimal("0.00")
    assert type(result) == Decimal
