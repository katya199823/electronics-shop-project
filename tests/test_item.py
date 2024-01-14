"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
import pathlib

@pytest.fixture
def item_fixture():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item_fixture):
    assert item_fixture.calculate_total_price() == 200000


def test_apply_discount(item_fixture):
    Item.pay_rate = 0.8
    item_fixture.apply_discount()
    assert item_fixture.price == 8000.0


def test_item_all(fixture_class_item, fixture_class_item_2):
    for value in Item.all:
        assert isinstance(value, object)


def test_getter_and_setter(item_fixture):
    item = item_fixture
    item.name = "smartphoneOne"
    assert item.name == "Smartphone"

    item.name = "smart"
    assert item.name == "Smart"

    item.name = 111
    assert item.name == "111"


def test_instantiate_from_csv():
    ROOT = pathlib.Path(__file__).parent.parent
    Item.instantiate_from_csv(pathlib.Path.joinpath(ROOT / 'src/items.csv'))

    assert len(Item.all) == 5

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('2') == 2
    assert Item.string_to_number('2.5') == 2
    assert Item.string_to_number('2,5') == 2