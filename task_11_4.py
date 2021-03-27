class ComplexNumber:
    def __init__(self, real, imaginary):    #Если Вам нужна только мнимая часть, на место 1-ого аргумента поставьте 0

        self.real = real
        self.imaginary = imaginary
        try:
            self.real = int(self.real) if not isinstance(self.real, float) else self.real
            self.imaginary = int(self.imaginary) if not isinstance(self.imaginary, float) else self.imaginary
        except ValueError:
            print('ОШИБКА\nВведите действительное число')




    def __str__(self):
        return f'Алгебраическая форма:\n{self.real} + {self.imaginary}i'


    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)



    def __mul__(self, other):
        real = self.real*other.real - self.imaginary*other.imaginary
        imaginary = self.real*other.imaginary + self.imaginary*other.real
        return ComplexNumber(real, imaginary)



z = ComplexNumber(0.1, 0)
x = ComplexNumber('1', 2)
print(z)
print(x)
