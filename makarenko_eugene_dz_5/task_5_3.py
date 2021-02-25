tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 'Андрей'

]
klasses = [
    '9А', '7В', '9Б'
]
gene = ((tutors[i], klasses[i]) if not i >= len(klasses) else (tutors[i], None) for i in range(len(tutors)))
while True:
    print(next(gene))