import csv
from pathlib import Path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []


    @property
    def name(self):
        """
        Возвращает приватное имя
        """
        return self.__name


    @name.setter
    def name(self, name):
        """
        Обрезает строку до 10 символов
        """
        self.__name = name.strip()[:10].capitalize()


    @classmethod
    def instantiate_from_csv(cls, csv_file):
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv
        """
        current_file_path = Path(__file__)
        csv_file = current_file_path.parent.parent / csv_file
        cls.all.clear()
        with open(csv_file, 'r', encoding='windows-1251') as csv_file:
            file = csv.DictReader(csv_file)

            for row in file:
                cls(row['name'], float(row['price']), float(row['quantity']))


    @staticmethod
    def string_to_number(string: str) -> int:
        """
        Статический метод, возвращающий число из числа-строки
        """
        clean_string = string.strip().replace(',', '.')
        return int(float(clean_string))


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f"{self.__name}"


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return None
