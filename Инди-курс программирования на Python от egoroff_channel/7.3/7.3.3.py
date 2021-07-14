"""
Напишите функцию first_unique_char,
которая принимает строку символов и возвращает позицию первого уникального символа в строке.
В случае, если уникальных символов в переданной строке нет, верните -1. Регистр символов не учитывайте.

Ваша задача написать только определение функции first_unique_char
"""


def first_unique_char(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return i
    return -1


print(first_unique_char('python'))
print(first_unique_char('abracadabra'))
print(first_unique_char('abcabc'))