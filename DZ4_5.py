# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

# На этом этапе мы просто использовали код из задачи №4 для генерации двух файлов содержащих многочлены.
# Для чтения 2-х файлов используемм функцию
def replaceFromFile(path: str):
    polyk = {}
    with open(path, 'r') as data:
        poly1 = data.readline()
    
    # Поскольку многочлены считываем из файла, где мы их создали в красивом виде в задаче 4.4, 
    # то надо привести к правильному виду ммногочлены у которых степень 1 и 0    
    poly1 = poly1.replace("*x ", "*x^1 "). replace(" =", "*x^0 ="). replace(" - ", " -"). replace(" + ", " "). replace("*x", "").split()

    for i in range(len(poly1)-2):
        poly1[i] = poly1[i].split("^")
    
    poly1 = poly1[:-2]
    for i in poly1:
       polyk[int(i[1])] = int(i[0])
    
    return polyk

stringPolyOne = replaceFromFile("poly45_1.txt")
print(stringPolyOne)
stringPolyTwo = replaceFromFile("poly45_2.txt")
print(stringPolyTwo)

resultPoly = {}
for i in range(max (len(stringPolyOne), len(stringPolyTwo)), -1, -1):
    first = stringPolyOne.get(i)
    second = stringPolyTwo.get(i)
    if first != None or second != None:
        resultPoly[i] = first + second

print(resultPoly)

result = ''

for i in resultPoly.items():
    if i[1] < 0:
        result += ' - ' + str(abs(i[1])) + 'x^' + str(i[0])
    elif i[1] > 0:
        result += ' + ' + str(abs(i[1])) + 'x^' + str(i[0]) 

result = result.replace(' - ', '-', 1)
result = ''.join((result, " = 0"))
print(result)

with open('poly45_result.txt', 'w', encoding='UTF-8') as ff:
    ff.write(result.replace('x^0', ''). replace('x^1', 'x')) # для красоты в файле убираем степени 0 и 1 в соответсивии с математикой:)
    
# Вариант не универсальный, т.к. сделан не для любого коэффициента степени:) Но как её сделать, мы разбирали и знаю.