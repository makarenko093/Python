f = open('dz.txt', 'rt', encoding='utf-8')
dicto = {}
spam = []
arr = ((x[0][:x[0].find(' ')], *x[1].split()[:2]) for x in (line.split('"') for line in f))
for el in arr:
    if el[0] in spam:
        if el[0] in dicto:
            dicto[el[0]] += 1
        else:
            dicto[el[0]] = 2
    else:
        spam.append(el[0])
for a, b in sorted(dicto.items(), key=lambda i: i[1], reverse=True)[:10]:
    print(f"ip address {a} : amount of requests {b}")
f.close()
