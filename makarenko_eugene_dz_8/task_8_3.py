from functools import wraps


def type_logger(func):
    def wrapper(*args, **kwargs):
        log = f'{func.__name__}('
        for x in args:
            log += f'{x}: {type(x)}, '
        for x, y in kwargs.items():
            log += f'{x}={y}: {type(y)}, '
        print(f'{log[:-2]})')
        return func(*args, **kwargs)

    return wrapper


def type_of_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'тип результата выполнения функции {type(result)}')
        return result

    return wrapper


@type_logger
@type_of_function
def mult(*args, **kwargs):
    res = 1
    for i in args:
        res *= i
    for i in kwargs.values():
        res *= i
    return res


a = mult(True, False)
print(a)
