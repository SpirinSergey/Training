"""
Быстрая сортировка (quick sort) | Разбор

Быстрая сортировка - еще один вид сортировки, который использует рекурсию.

Ваша задача реализовать этот алгоритм. Для этого нужно будет создать функцию quick_sort,
которая будет принимать исходный список и возвращать новый отсортированный в порядке неубывания список.

Необходимо написать только определение функций quick_sort,
при этом нельзя пользоваться встроенными сортировками в Python
"""


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    el = lst[0]
    left = list(filter(lambda x: x < el, lst))
    center = [_ for _ in lst if _ == el]
    right = list(filter(lambda x: x > el, lst))
    return quick_sort(left) + center + quick_sort(right)


print(quick_sort([19, 4, 5, 17, 1]))  # 1 4 5 17 19
print(quick_sort([16, 19, 2, 12, 20, 15, 20, 15]))  # 2 12 15 15 16 19 20 20
