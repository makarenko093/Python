"""4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат."""


class Car:

    def __init__(self, color, name):
        self._speed = 0
        self.color = color
        self.name = name
        self._is_police = False

    def go(self, speed):
        self._speed = speed
        print('Машина поехала')

    def brake(self):
        self._speed = 0
        print('Машина остановилась')

    def turn(self, dirrection='право'):
        print(f'The {self.name} turned {dirrection}')

    def show_speed(self):
        print(f'{self._speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'{self._speed}') if self._speed <= 60 else print(f'Вы превысили скорость, ограничение 60')



class SportCar(Car):
    pass



class WorkCar(Car):
    def show_speed(self):
        print(f'{self._speed}') if self._speed <= 40 else print(f'Вы превысили скорость, ограничение 40')



class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)
        self._is_police = True



workCar = WorkCar('black', 'kamaz')
townCar = TownCar('black', 'mazda')
policeCar = PoliceCar('white', 'УАЗ')
sportCar = SportCar('pink', 'BMW')

workCar.go(60)
print(policeCar._is_police)
print(sportCar._speed)
sportCar.go(100)
sportCar.show_speed()
workCar.show_speed()
workCar.brake()
workCar.show_speed()
print(workCar._is_police)