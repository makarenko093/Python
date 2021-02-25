def gen(n):
    for i in range(1, n + 1, 2):
        yield i


a = gen(9)
next(a)
next(a)
next(a)
next(a)
next(a)
#next(a)

def gen(n):
    for i in range(1, n + 1, 2):
        if i**2 <= 200: yield i

a = gen(200)
print(tuple(a))


def gen(n):
    sm = 0
    for i in range(1, n + 1, 2):
        sm += i
        yield i, sm

x = gen(14)
print(*x)
