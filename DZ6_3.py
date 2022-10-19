# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь,
# ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.


def get_list(n: int):
    people = [input('Введите имя: ') for _ in range(n)]
    return people


def get_dict(list_p: list):
    result = {}
    for name in list_p:
        key = name[0]
        if key not in result:
            result[key] = []
        result[key].append(name)
    return result


n = int(input('Cколько у вас сотрудников? '))
my_pep = get_list(n)
print(my_pep)
print(get_dict(my_pep))