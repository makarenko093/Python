import os
import json
def counter(dirr):
    dictionary = {}
    for paths, dirs, files in os.walk(os.path.join('.', dirr)):
        for file in files:
            path = os.path.relpath(os.path.join(paths, file), os.getcwd())
            rang = 10 ** (len(str(os.stat(path).st_size))) if os.stat(path).st_size else 0
            ext = file.rsplit('.', maxsplit=1)[-1]
            if rang not in dictionary:
                dictionary[rang] = [1, [ext]]
            else:
                dictionary[rang][0] += 1
            dictionary[rang][1].append(ext) if ext not in dictionary[rang][1] else 1

    return dictionary

if __name__ == '__main__':
    with open('task_7_5_summary.json', 'wt', encoding='utf-8') as f:
        f.write(json.dumps(counter('my_project'), sort_keys=True))
