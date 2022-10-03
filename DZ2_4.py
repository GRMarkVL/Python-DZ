
first_position = int(input('Enter a first position: ')) - 1
second_position = int(input('Enter a second position: ')) - 1
number = int(input('Enter a number of elements: '))

if first_position > (number * 2 + 1) or second_position > (number * 2 + 1):
    print('Error input')
elif first_position < 0 or second_position < 0:
    print('Error input')
else:
    list_numbers = []
    for i in range(-number, number + 1):
        list_numbers.append(i)
    print(f'-> {list_numbers}')
    res = list_numbers[first_position] * list_numbers[second_position]
    print(res)