class MyOwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        a = int(input('Делимое '))
        b = int(input('Делитель '))
        if b == 0:
            raise MyOwnError('На ноль делить нельзя, попробуйте еще раз')

    except MyOwnError as e:
        print(e)

    except ValueError as e:
        print(e)
    else:
        print(a/b)
        break

