def editor(n, value):
    for i in range(n - 1):
        file.readline()
    pos = file.tell()
    string = len(file.readline())
    if string:
        if string < len(value) + len(str(n)) + 1:
            the_rest = file.read()
            file.seek(pos)
            file.write(f"{n}:{value}\n{the_rest}")
        else:
            file.seek(pos)
            diff = string - (len(value) + len(str(n)) + 2)
            file.write(f"{n}:{value}{' '*diff}\n")
    else:
         print('Такой записи не существует')



if __name__ == '__main__':
    from sys import argv
    with open('bakery.scv', 'r+t', encoding='utf-8') as file:
        editor(int(argv[1]), argv[2])

