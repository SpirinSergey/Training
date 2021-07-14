"""
Напишите программу, которая считывает строку с числом nn, которое задаёт количество чисел, которые нужно считать.
Далее считывает nn строк с числами x_ix
i
​
 , по одному числу в каждой строке. Итого будет n+1n+1 строк.

При считывании числа x_ix
i
​
  программа должна на отдельной строке вывести значение f(x_i)f(x
i
​
 ). Функция f(x) уже реализована и доступна для вызова.

Функция вычисляется достаточно долго и зависит только от переданного аргумента xx. Для того,
чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.
"""

n = int(input())
d = dict()
for el in range(n):
    e = int(input())
    if e in d:
        print(d[e])
    else:
        d[e] = f(e)
        print(d[e])

