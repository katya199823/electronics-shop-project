"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import pathlib
from src.phone import Phone
from src.item import Item, InstantiateCSVError


@pytest.fixture
def item_fixture():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item_fixture):
    assert item_fixture.calculate_total_price() == 200000


def test_apply_discount(item_fixture):
    Item.pay_rate = 0.8
    item_fixture.apply_discount()
    assert item_fixture.price == 8000.0


def test_getter_and_setter(item_fixture):
    item = item_fixture
    item.name = "smartphoneOne"
    assert item.name == "smartphone"

    item.name = "smart"
    assert item.name == "smart"

    item.name = "111"
    assert item.name == "111"


def test_instantiate_from_csv():
    ROOT = pathlib.Path(__file__).parent.parent
    Item.instantiate_from_csv(pathlib.Path.joinpath(ROOT / 'src/items.csv'))

    assert len(Item.all) == 5

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_instantiate_from_csv_broken_file():
    with pytest.raises(InstantiateCSVError):
        assert Item.instantiate_from_csv(
            "../src/item_broken.csv") == "Файл item.csv поврежден"


def test_instantiate_from_csv_no_file():
    with pytest.raises(FileNotFoundError):
        assert Item.instantiate_from_csv(
            "item.csv") == "Отсутствует файл item.csv"


def test_string_to_number():
    assert Item.string_to_number('2') == 2
    assert Item.string_to_number('2.5') == 2
    assert Item.string_to_number('2,5') == 2


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


phone1 = Phone("iPhone 14", 120_000, 5, 2)
item2 = Item("Смартфон", 10000, 20)


def test_add():
    assert item2 + phone1 == 25
    assert phone1 + phone1 == 10
