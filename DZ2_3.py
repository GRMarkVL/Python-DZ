
# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

length = int(input('"Введите число:'))
s = []

for i in range(1, length + 1):
    s.append(round((1 + 1/i) ** i))

print(f'n = {length}: {s} -> {sum(s)}')

sum_s = 0
for i in range(length):
    sum_s += s[i]

print(f'n = {length}: {s} -> {sum_s}')