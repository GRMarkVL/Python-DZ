
# 4. * Функция принимает в качестве аргументов строки в формате «Имя Фамилия»,
# возвращает словарь, ключи — первые буквы фамилий, значения — словари, реализованные по схеме предыдущего задания.

def num_tes(names: str):
    names = names.split(', ')
    result = {}
    for name in names:
        index = name.index(' ')
        key = name[index+1]
        if key not in result:
            result[key] = []
        result[key].append(name)
    return result


name_list = 'Иван Сергеев, Инна Серова, Петр Алексеев, Илья Иванов, Анна Савельева, Юнона Ветрякова, Борис Аркадьев, Антон Серов, Павел Анисимов'
print(num_tes(name_list))