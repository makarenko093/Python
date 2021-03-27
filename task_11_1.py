import re
class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def to_extract(cls, el):
        try:
            for a, b in cls.is_valid(el.date).groupdict().items():
                print(a + ":", b)
        except AttributeError:
            print('Функция не работает')



    @staticmethod
    def is_valid(date):
        RE = re.match(r'^(?P<day>0?[1-9]|[12][0-9]|3[01])[-/\s.](?P<month>0?[1-9]|1[0-2])[-/\s.](?P<year>[12]\d{3}$|\d{2}$)', date)
        if not RE:
            return False
        else:
            return RE


if __name__ == '__main__':

    a = Date('19.13.1993')

    Date.to_extract(a)


