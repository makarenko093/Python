"""2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т."""

class Road:
    __mass = 24.6 #(кг) Толщина асфальта для покрытия 1 квадртного  м. дороги с толщиной 1 см
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculation(self, thickness=3):
        self.__thickness = thickness
        return int(self.__length * self.__width * self.__mass * self.__thickness)


a = Road(100, 10)
print(a.calculation(10))
b = Road(10, 3)
print(b.calculation(5))