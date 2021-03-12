import os
def counter(dir):
    dictionary = {}
    for paths, dirs, files in os.walk(os.path.join('.', dir)):
        for file in files:
            path = os.path.relpath(os.path.join(paths, file), os.getcwd())
            rang = 10 ** (len(str(os.stat(path).st_size))) if os.stat(path).st_size else 0
            if rang not in dictionary:
                dictionary[rang] = 1
            else:
                dictionary[rang] += 1
    return dictionary

if __name__ == '__main__':
    for key, val in sorted(counter('my_project').items()):
        print(f'{key}: {val}')