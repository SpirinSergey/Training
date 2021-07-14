"""
Напишите функцию list_sum_recursive,
которая принимает на вход список из целых чисел и возвращает сумму элементов переданного списка.
Не забывайте, что реализовать это нужно при помощи рекурсии.

Ваша задача только написать определение функции list_sum_recursive
"""


def list_sum_recursive(s):
    if len(s) == 0:
        return s[0]
    elif len(s) == 1:
        return s[0]
    else:
        return list_sum_recursive(s[0:1]) + list_sum_recursive(s[1:])


