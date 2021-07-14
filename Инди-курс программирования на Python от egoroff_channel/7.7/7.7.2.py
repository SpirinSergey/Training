"""
Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

Требуется найти N-е число Фибоначчи.

Входные данные
Программе поступает на вход целое число N (0 ≤ N ≤ 30) - порядковый номер числа Фибоначчи.

Выходные данные
Вам необходимо вывести на экран N-е число Фибоначчи.
"""


def fbn(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fbn(n - 1) + fbn(n - 2)


print(fbn(int(input())))


