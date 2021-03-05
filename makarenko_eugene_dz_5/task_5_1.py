gen1 = (i for i in range(1, 11, 2))
list(gen1)
print(next(gen1))


gen2 = (i for i in range(1, 101, 2) if i**2 <= 200)
print(next(gen2))
print(tuple(gen2))
# print(next(gen2))