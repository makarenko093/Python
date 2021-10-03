class DigitsChecker(Exception):
    def __init__(self, *txt):
        if txt:
            self.txt = txt[0]
        else:
            self.txt = None


lst = []
while True:
    x = input('Введите число ')
    try:
        try:
            x = int(x)
        except ValueError:
            raise DigitsChecker('Введите число', x)
    except DigitsChecker as e:
        if e.args[1].lower() == 'stop':
            break
        else:
            print(e.args[1])
            print(f'{e.args[1]}: не прошло проверку')
    else:
        lst.append(x)


print(lst)




