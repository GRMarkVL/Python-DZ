# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

n = int(input("Введите длину списка: "))

def randomList(n):
    list = []
    for i in range(n):
        list.append(random.randint(0, 10))
    return list

listMy = randomList(n)
print(listMy)

lenght = int(len(listMy) / 2)

if len(listMy) % 2 != 0:
    resultList = []
    for i in range(lenght + 1):
        num = listMy[i] * listMy[len(listMy) - i - 1]
        resultList.append(num)
else:
    resultList = []
    for i in range(lenght):
        num = listMy[i] * listMy[len(listMy) - i - 1]
        resultList.append(num)
print(resultList)