import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "грязный"]
something = ["asdds", "asdgjj"]

def get_jokes(*args, n=1, repeatable=True):  # *args - коллекция списков, n - кол. шуток
    if repeatable:
        jokes = []
        for i in range(n):
            joke = []
            for el in args:
                joke.append(random.choice(el))
            jokes.append(" ".join(joke))
        return jokes
    else:
        n = len(min(args, key=len)) if len(min(args, key=len)) < n else n
        jokes = []
        for i in range(n):
            joke = []
            for el in args:
                joke.append(el.pop(random.randrange(len(el))))
            jokes.append(" ".join(joke))
        return jokes


print(get_jokes(nouns, adverbs, adjectives, something, n=10, repeatable=False))
