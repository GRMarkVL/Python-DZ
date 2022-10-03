
# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
from random import randint

length = int(input('Введите число: '))
s = list(range(length))

print(f'n = {length}: {s}')

for i in range(length):
    ran = randint(0, length-1)
    s[i], s[ran] = s[ran], s[i]

print(f'-> {s}')

for i in range(length):
    temp = s[i]
    ran = randint(0, length-1)
    s[i] = s[ran]
    s[ran] = temp

print(f'-> {s}')