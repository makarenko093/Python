import os

with open('yaml.txt', 'rt', encoding='utf-8') as f:
    file = f.read().splitlines()
    path = os.path.join('.', file[0].split()[-1].lstrip('|--'))
    os.makedirs(path, exist_ok=True)
    for i in range(1, len(file)):
        el = file[i].split()[-1].lstrip('|--')
        if len(file[i].split(' ')) >= len(file[i - 1].split(' ')):
            if '.' in el:
                fpath = os.path.join(path, el)
                with open(fpath, 'w', encoding='utf-8'):
                    pass
            else:
                path = os.path.join(path, el)
                os.makedirs(path, exist_ok=True)
        else:
            path = os.path.join('.', file[0].split()[-1].lstrip('|--'), el)
            os.makedirs(path, exist_ok=True)