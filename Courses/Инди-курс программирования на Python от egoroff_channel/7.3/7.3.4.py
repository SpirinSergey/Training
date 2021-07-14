"""
Ваша задача написать функцию format_namelist, которая принимает список словарей,
у каждого словаря в списке есть только ключ name

Функция format_namelist должна вернуть отформатированную строку,
в которой все имена из списка разделяются запятой кроме последних двух имен, они должны быть разделены союзом "и".
Если в списке нет ни одного имени, функция должна вернуть пустую строку. Ниже представлены примеры:

format_namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa и Maggie'

format_namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart и Lisa'

format_namelist([ {'name': 'Bart'} ])
# returns 'Bart'

format_namelist([])
# returns ''
"""


def format_namelist(dict_lst):
    list_name = []
    if len(dict_lst) == 0:
        return str()
    for el in dict_lst:
        for value in el.values():
            list_name.append(value)
    if len(list_name) == 1:
        return str(*list_name)
    elif len(list_name) == 2:
        return ' и '.join(list_name)
    else:
        return ', '.join(list_name[:-1]) + ' и ' + str(list_name[-1])


print(format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
# returns 'Bart, Lisa и Maggie'

print(format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
# returns 'Bart и Lisa'

print(format_namelist([{'name': 'Bart'}]))
# returns 'Bart'

print(format_namelist([]))
# returns ''
