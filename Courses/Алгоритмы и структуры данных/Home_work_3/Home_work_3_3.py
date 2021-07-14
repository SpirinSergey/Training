# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы. +

from random import randint

max_num = 0
min_num = 1000

start_list = [randint(1, 1000) for i in range(5)]
print(f'Массив случайных чисел - {start_list}')

for i, item in enumerate(start_list):

    if item > max_num:
        max_num = item
        i_max = i
    if item < min_num:
        min_num = item
        i_min = i

start_list[i_max], start_list[i_min] = start_list[i_min], start_list[i_max]

print(f'Новый массив - {start_list}')
