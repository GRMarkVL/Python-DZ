# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from unittest import result


list = [1.1, 1.2, 3.1, 5, 10.01]

newList = [] 

for i in range(len(list)): 
    num = round((list[i] % 1), 2) 
    newList.append(num)

print(newList)  

def minimum(list): 
    min = list[0]
    for i in range(1, len(list)):
        if list[i] < min and list[i] != 0: 
            min = list[i]
    return min

def maximum(list): 
    max = list[0]
    for i in range(1, len(list)):
        if list[i] > max:
            max = list[i]
    return max

result = maximum(newList) - minimum(newList)
print(result)