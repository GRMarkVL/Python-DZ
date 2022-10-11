
# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности. Решать через множества и еще каким-нибудь способом кроме множества
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []
from collections import Counter

num = str(input("Введите число: "))

myList = []
for i in range(len(num)):
    myList.append(int(num[i]))

counter = Counter(myList)

newList = []
for key, value in counter.items():
    if value == 1:
        newList.append(key)
print(newList)


setList = set(myList)

# newListFor = []     
# for i in range(len(myList)):
#     # for j in range(i+1, len(myList)):
#     #     print(j, ',')
#     if myList[i] != myList[i+1]:
#         newListFor.append(myList[i])


# print(newListFor)