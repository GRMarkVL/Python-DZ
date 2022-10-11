# Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

from decimal import Decimal
import math
from random import Random, uniform
import random

#Вычисление pi по формуле Беллара
def bbp(n): 
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(1) / (16**k)) * ((Decimal(4) / (8 * k + 1)) - (Decimal(2) / (8 * k + 4)) - (Decimal(1) / (8 * k + 5)) - (Decimal(1) / (8 * k + 6)))
        k += 1
    return pi

numPi = bbp(2)
print(bbp(2))

randIn = random.randint(2, 7)
print(randIn)

# Просто количество после запятой
print("{:.{}f}".format(numPi, randIn))


# d = 1 / 10**randIn # Задание произвольного предела от сгенерированного
# print(d)

# Задание предела через ввод пользователя
d = float(input("Введите количество чисел по шаблону в пределах от 0.1 до 0.0000000001: "))

print(d)
count = 0
while d < 1:
    d = d * 10
    count = count + 1
    
print(count)
print("{:.{}f}".format(numPi, count)) # Вывод количества после запятой при задании пользователем с клавиатуры по шаблону в пределах