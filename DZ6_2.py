
# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
from curses.ascii import isdigit
from random import randint


def new_list(n: int):
    my_list = list(range(20, n+1))
    return my_list


def is_multiple(num: list, a=20, b=21):
    result = [i for i in num if not i % a or not i % b]
    return result


n = input('Put the last number: ')
if n.isdigit():
    my_list = new_list(int(n))
    print(my_list)
else:
    print('It is not a number')

print(is_multiple(my_list))