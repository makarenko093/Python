class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number - other.number > 0:
           return Cell(self.number - other.number)
        else:
            print('Операцию невозможно выполнить')

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __floordiv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, divider):
        string = ""
        for i in range(1, self.number + 1):
            if i % divider:
                string += '*'
            else:
                string += '*\n'

        return string



a = Cell(11)
b = Cell(10)
c = a * b
c = c + a

print(c.number)
print(c.make_order(10))