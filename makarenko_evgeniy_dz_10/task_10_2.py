"""2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property."""
from abc import ABC, abstractmethod

class Clothing(ABC):
    __consumption = 0
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calc(self):
        pass

    @property
    def consumption(self):
        return Clothing.__consumption

    @consumption.setter
    def consumption(self, new_value):
        Clothing.__consumption = new_value




class Suit(Clothing):

    def __init__(self, height):
        self.height = height
        self.type = 'suit'
        self.consumption += self.calc()


    def calc(self):
        return round(2*self.height + 0.3, 3)


class Coat(Clothing):
    def __init__(self, size):
        self.size = size
        self.type = 'coat'
        self.consumption += self.calc()


    def calc(self):
        return round(self.size / 6.5 + 0.5, 3)


a = Coat(10)
b = Coat(10)
c = Suit(13)
print(a.calc())
print(b.calc())
print(c.calc())
print(a.consumption)
print(Clothing._Clothing__consumption)