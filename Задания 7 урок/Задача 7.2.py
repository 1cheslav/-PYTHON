# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes:
    def __init__(self, name, coat_size=None, height_suit=None):
        self.name = name
        self.coat_size = coat_size
        self.height_suit = height_suit


class Coat(Clothes):
    @property
    def con_coat(self):
        return int(self.coat_size/6.5 + 0.5)


class Suit(Clothes):
    def con_suit(self):
        return int(self.height_suit * 2 + 0.3)


coat = Coat("Пальто", 54)
suit = Suit("Костюм", None, 1.75)
print(f"Расход ткани для пальто - {coat.con_coat}м")
print(f"Расход ткани для костюма - {suit.con_suit()}м")
print(f"Общий расход ткани - {coat.con_coat + suit.con_suit()}м")


class Clothes(ABC):
    @abstractmethod
    def __init__(self, name, coat_size=None, height_suit=None):
        self.name = name
        self.coat_size = coat_size
        self.height_suit = height_suit


class Coat(Clothes):
    def __init__(self, name, coat_size=None, height_suit=None):
        self.name = name
        self.coat_size = coat_size
        self.height_suit = height_suit

    def con_coat(self):
        return int(self.coat_size/6.5 + 0.5)


class Suit(Clothes):
    def __init__(self, name, coat_size=None, height_suit=None):
        self.name = name
        self.coat_size = coat_size
        self.height_suit = height_suit

    def con_suit(self):
        return int(self.height_suit * 2 + 0.3)


print()
coat = Coat("Пальто", 54)
suit = Suit("Костюм", None, 1.75)
print(f"Расход ткани для пальто - {coat.con_coat()}м")
print(f"Расход ткани для костюма - {suit.con_suit()}м")
print(f"Общий расход ткани - {coat.con_coat() + suit.con_suit()}м")



