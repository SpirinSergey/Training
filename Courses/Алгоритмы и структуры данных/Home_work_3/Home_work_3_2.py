# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3,15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните,
# что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа. +

from random import randint

new_list = []

start_list = [randint(1, 100) for i in range(20)]
print(f'Массив случайных чисел - {start_list}')

for i, el in enumerate(start_list):
    if el % 2 == 0:
        new_list.append(i)

print(f'Индексы четных элементов - {new_list}')