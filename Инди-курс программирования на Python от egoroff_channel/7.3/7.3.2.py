"""
Ваша задача написать функция find_duplicate, которая принимает один аргумент - список чисел.
Функция должна возвращать список из дублей, каждый дубль нужно брать только один раз в том порядке,
в котором они встречаются в исходном списке. Под дублем будем подразумевать число,
которое присутствовало в списке несколько раз.

Ваша задача написать только определение функции
"""

def find_duplicate(lst):
    new_lst = []
    for el in lst:
        if lst.count(el) > 1:
            if el not in new_lst:
                new_lst.append(el)
    return new_lst


print(find_duplicate([2, 2, 3, 3, 5, 5, 2]))
print(find_duplicate([1, 2, 3, 4, 5, 6]))
print(find_duplicate([2, 2, 2, 3, 3, 3]))
print(find_duplicate([]))
