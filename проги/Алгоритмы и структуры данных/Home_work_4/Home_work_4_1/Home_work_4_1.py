# Задача - Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3,15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните,
# что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.

import cProfile
from random import randint

def pos_lst(range_num, len_list):
    new_list = []
    start_list = [randint(1, range_num) for i in range(len_list)]
    print(f'Массив случайных чисел - {start_list}')

    for i, el in enumerate(start_list):
        if el % 2 == 0:
            new_list.append(i)

    print(f'Индексы четных элементов - {new_list}')


# pos_lst(100, 20)

# cProfile.run('pos_lst(100, 20)')
# 120 function calls in 0.000 seconds
# 50 loops, best of 5: 635 usec per loop

# cProfile.run('pos_lst(100, 200)')
# 1166 function calls in 0.001 seconds
# 50 loops, best of 5: 1.54 msec per loop

# cProfile.run('pos_lst(100, 20000)')
# 115443 function calls in 0.084 seconds
# 50 loops, best of 5: 80.7 msec per loop







