from sys import argv
if len(argv) == 1:
    with open('bakery.scv', 'rt', encoding='utf-8') as f:
        print(f.read())
elif len(argv) == 2:
    with open('bakery.scv', 'rt', encoding='utf-8') as f:
        for i in range(int(argv[1]) - 1):
            f.readline()
        print(f.read())


elif len(argv) == 3:
    with open('bakery.scv', 'rt', encoding='utf-8') as f:
        for i in range(int(argv[1]) - 1):
            f.readline()
        for i in range(int(argv[2]) - int(argv[1]) + 1):
            print(f.readline().strip())



