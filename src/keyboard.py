# - \* - coding: utf-8 - \* -
from src.item import Item

class Language:
    def __init__(self, language: str = "EN") -> None:
        """ Инициализация атрибута класса """
        self.__language = language

    @property
    def language(self) -> str:
        """ Возвращает язык раскладки клавиатуры """
        return self.__language

    def change_lang(self) -> 'Language':
        """ Меняет язык раскладки """

        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self

class Keyboard (Item, Language):
    """ Класс для представления клавиатуры в магазине. """
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """ Инициализация атрибутов класса """
        super().__init__(name, price, quantity)
        Language.__init__(self)

    def __repr__(self):
        """
        Возвращает информацию об объекте
        """
        return f"Keyboard({self.name}, {self.price}, {self.quantity}, {self.__language})"