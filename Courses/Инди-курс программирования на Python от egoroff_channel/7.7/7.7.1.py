"""
Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.

Входные данные
Программа принимает на вход натуральное число N (N ≤ 103). Во второй строке через пробел идут N целых чисел,
по модулю не превосходящих 103 - элементы последовательности.

Выходные данные
Ваша задача вывести заданную последовательность в обратном порядке.
"""


def back(x, list_num):
    if x != 0:
        list_num = [el for el in list_num.split()]
        print(list_num[-1], end=' ')
        x = int(x) - 1
        list_num = ' '.join(list_num[:-1])
        back(x, list_num)


back(input(), input())


