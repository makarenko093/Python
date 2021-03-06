from sys import exit
import json
with open('hobbies.csv', 'r', encoding='utf-8') as f2, open('users.csv', 'r', encoding='utf-8') as f, open('dictionary.py', 'w', encoding='utf-8') as f3:
    users = [' '.join(x.split(',')).strip() for x in f.readlines()]
    hobbies = [', '.join(x.split(',')).strip() for x in f2.readlines()]
    if len(hobbies) > len(users):
        d = {a: b for a, b in zip(users, hobbies)}
        json.dump(d, f3, indent=3, ensure_ascii=False)
        exit(1)
    else:
        d = {users[i]: (hobbies[i] if i < len(hobbies) else None) for i in range(len(users))}
        json.dump(d, f3, indent=1 , ensure_ascii=False)
    print(d)