from functools import wraps
def val_checker(condition):
    def logger(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in args:
                if not condition(i):
                    raise ValueError(f'wrong value: {i}, {type(i)}')
            for i in kwargs.values():
                if not condition(i):
                    raise ValueError(f'wrong value: {i}, {type(i)}')
            return func(*args, **kwargs)
        return wrapper
    return logger

@val_checker(lambda x: isinstance(x, int) or isinstance(x, float))
def mult(*args, **kwargs):
    res = 1
    for i in args:
        res *= i
    for i in kwargs.values():
        res *= i
    return res


a = mult(2, y=1, d=5.6)
print(a)
print(mult.__name__)

