arr = list(map(lambda item: item**3, list(range(1, 1001, 2))))

#a:

total = 0
for number in arr:
    length = 1
    while number // 10**length:
        length += 1
    sumofnumber = number % 10
    for i in range(length, 0, -1):
        sumofnumber += number // 10**i % 10
    if sumofnumber % 7 == 0:
        total += sumofnumber
print(total)


#b, c
for i in range(len(arr)):
    arr[i] += 17
total2 = 0
for number in arr:
    length = 1
    while number // 10**length:
        length += 1
    sumofnumber = number % 10
    for i in range(length, 0, -1):
        sumofnumber += number // 10**i % 10
    if sumofnumber % 7 == 0:
        total2 += sumofnumber

print(total2)
