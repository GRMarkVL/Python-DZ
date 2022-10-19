
# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
import numbers
from random import randint


def new_list(n: int):
    my_list = [randint(1, 101) for _ in range(n)]
    return my_list


def sort_list(numbers: list):
    sort_num = [numbers[i]
                for i in range(1, len(numbers)) if numbers[i] > numbers[i-1]]
    return sort_num


n = int(input('Put the number: '))
task = new_list(n)
print(task)
sorted_task = sort_list(task)
print(sorted_task)