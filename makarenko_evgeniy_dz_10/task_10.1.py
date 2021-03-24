class Matrix:
    def __init__(self, massive):
        self.massive = massive




    def __str__(self):
        self.length = max(len(el) for el in self.massive)
        string = ""
        for x in self.massive:
            if len(x) == self.length:
                string += '\n' if string else ""
                for x in x:
                    if isinstance(x, int):
                        string += f'{x} '
                    else:
                        raise ValueError('wrong input')
            else:
                raise ValueError('wrong input')
        return string













a = Matrix([[1, 9, 3], [1, 2, -3], [1, 2, 3]])

print(a)
