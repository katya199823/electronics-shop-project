# - \* - coding: utf-8 - \* -
import pytest
from src.item import Item
from src.phone import Phone

phone1 = Phone("iPhone 14", 120_000, 5, 2)
item1 = Item("Смартфон", 10000, 20)


def test_str():
    assert str(phone1) == 'iPhone 14'


def test_repr():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_get_number_of_sim():
    assert phone1.number_of_sim == 2


def test_exc_number_of_sim():
    with pytest.raises(ValueError):
        phone1.number_of_sim = -1


def test_add():
    assert phone1 + item1 == 25
    assert phone1 + phone1 == 10
