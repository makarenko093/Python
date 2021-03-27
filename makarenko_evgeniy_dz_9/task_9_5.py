'''5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''

class Stationery:
    title = 'Канцелярская принадлежность'

    def draw(self):
        print('запук отрисовки')


class Pen(Stationery):
    title = 'Ручка'

    def draw(self):
        print('запуск отрисовки ручкой')


class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self):
        print('запуск отрисовки карандашем')


class Handle(Stationery):
    title = 'Маркер'

    def draw(self):
        print('запуск отрисовки маркером')

a = Handle()
b = Pen()
c = Pencil()
print(a.title)
print(b.title)
print(c.title)