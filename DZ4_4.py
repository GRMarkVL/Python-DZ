
# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующая степень следующего многочлена на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
#
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

import random

k = int(input("Введите число: "))

list = []
for i in range(k+1):
    num = random.randint(-100, 100) #Генерируем случайные множители в количестве равному максимальному коэффициенту k
    list.append(num)
print(list)

myNewList = []

for i in range(k, -1, -1):
    if list[i] != 0:  # Если множитель = 0, игнорируем его, если не= 0, тогда запускаем сборку
        if i == 0:
            myNewList.append(str(list[i])) # Собираем строчку формулы для нулевой степени
        elif i == 1:
            myNewList.append(str(list[i]) + "*x") # Собираем строчку формулы 
        else:
            myNewList.append(str(list[i]) + "*x" + "^" + str(i)) # Собираем строчку формулы 
# print(myNewList)

newString = ""
for i in myNewList:
    newString += str(i) + " " #Переводим список в строку
# print(newString)

l = len(newString)
removeLast = newString[:l-1] #Убираем последний символ (в нашем случае это лишний пробел, который заменился на лишний плюс)

removeLast = removeLast.replace(' ', ' + ')   #Заменяем пробелы на +
removeLast = removeLast.replace('+ -', '- ')   # Если число отрицательное, убираем лишний + и пробел"

removeLast = ''.join((removeLast, " = 0")) # Добавляем в конец формулы ""= 0"
print(removeLast)

with open('poly.txt', 'w', encoding='UTF-8') as ff:
    ff.write(removeLast)