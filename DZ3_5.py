# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fibonacciMy(n):
    fib1 = fib2 = 1 
    
    fibanacciList = []  
    for i in range(n+1):
        fib1, fib2 = fib2, fib1 - fib2
        fibanacciList.append(fib2)
        
    fibanacciList = fibanacciList[::-1]     
     
    fb1 = fb2 = 1
    fibanacciList.insert(i+1, 1)     
    fibanacciList.insert(i+1, 1)
    
    for i in range(2, n):
        fb1, fb2 = fb2, fb1 + fb2
        fibanacciList.append(fb2)    
    return fibanacciList

num = int(input("Введите длину списка: "))

listMy = fibonacciMy(num)
print(listMy)