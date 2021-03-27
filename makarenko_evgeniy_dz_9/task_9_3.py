"""3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров."""
A = {'wage': 1000, 'bonus': '10%'}
B = {'wage': 2000, 'bonus': '12%'}
class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name.title()
        self.surname = surname.title()
        self.position = position
        self._income = income


class Position(Worker):


    def get_full_name(self):
        return  f'{self.name} {self.surname}'


    def get_total_income(self):
        wage, bonus = self._income.values()
        return int(wage*(1 + int(bonus[:-1])/100))


a = Position('алексей', 'овчинников', 'охранник', A)
print(a.get_full_name())