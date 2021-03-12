from sys import argv
for i in range(1, len(argv)):
    with open('bakery.scv', 'at', encoding='utf-8') as f:
        f.write(argv[i] + "\n")