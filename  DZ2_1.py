# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

n = float(input("Введите число: "))

suma = 0

if (n % 1 != 0):
    while n % 1 != 0:
        n = n * 1000
        print(n)
    while n > 0:
        digit = n % 10
        suma = suma + digit
        n = n // 10  
else: 
    while n > 0:
        digit = n % 10
        suma = suma + digit
        n = n // 10
    
print("Сумма:", suma)