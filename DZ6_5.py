
# 5. ** Реализовать функцию, возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)


from random import choice


def get_jokes(num:int):

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    list_jokes = []
    for joke in range(num):
        list_jokes.append(
            f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')

    return list_jokes

n=int(input('Сколько вы хотите шуток? '))
print(get_jokes(n))