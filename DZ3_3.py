# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from unittest import result


list = [1.1, 1.2, 3.1, 5, 10.01]

newList = [] #Собираем в список дробные части значений элементов списка

for i in range(len(list)): #С помощью цикла перебираем все элементы и записываем дробную часть в список
    num = round((list[i] % 1), 2) #округляем
    newList.append(num)

print(newList)  #Печатаем список для наглядности

def minimum(list): #Функция определения минимального значения
    min = list[0]
    for i in range(1, len(list)):
        if list[i] < min and list[i] != 0: #исключаем из вычисления минимально значения то, у которого дробная часть осутствует
            min = list[i]
    return min

def maximum(list): #Функция определения максимального значения
    max = list[0]
    for i in range(1, len(list)):
        if list[i] > max:
            max = list[i]
    return max

result = maximum(newList) - minimum(newList)
print(result)