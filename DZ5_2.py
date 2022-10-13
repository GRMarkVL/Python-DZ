# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Кодирование длин серий (англ. run-length encoding, RLE) или кодирование повторов 
# — алгоритм сжатия данных, заменяющий повторяющиеся символы (серии) 
# на один символ и число его повторов



def compression(my_text): #функция для сжатия текста
    index = 1 #счетчик. Как раз укажет количество букв по сжатию.
    result = '' #переменная для результата сжатия
    for i in range(len(my_text)-1): #для i по длине введенного текста
        if my_text[i] == my_text[i+1]: #если i-ый символ совпадает со след.симоволом
            index += 1 #увеличиваем индекс на 1
        else:
            # иначе: складываем наш посчитанный результат + счетчик букв + символ текста
            result = result + str(index) + my_text[i]
            index = 1
    if index > 1 or (my_text[len(my_text)-2] != my_text[-1]):
        result = result + str(index) + my_text[-1] 
    return result

def recovery(my_text): #функция для восстановления текста
    number = ''
    result = ''
    for i in range(len(my_text)):
        # проверяем, если строка состоит не только из буквенных символов, то:
        if not my_text[i].isalpha():
            number += my_text[i]
        else:
            # выводит количество букв восле цифры. 
            # Т.е. сколько раз в восстановленном тексте должна быть конкретная буква
            result = result + my_text[i] * int(number)
            number = ''
    return result


vvod = input("Введи текст для RLE алгоритма: ")
print(f"Текст после сжатия имеет вид: {compression(vvod)}")
print(f"Текст после восстановления имеет вид: {recovery(compression(vvod))}")