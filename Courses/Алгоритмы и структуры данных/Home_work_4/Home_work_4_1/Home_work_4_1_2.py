import cProfile
from random import randint


def pos_lst(range_num, len_list):
    new_list = []
    for i, el in enumerate([randint(1, range_num) for i in range(len_list)]):
        if el % 2 == 0:
            new_list.append(i)
    return new_list


# pos_lst(100, 20)

# cProfile.run('pos_lst(100, 20)')
# 119 function calls in 0.001 seconds
# 50 loops, best of 5: 25.7 usec per loop


# cProfile.run('pos_lst(100, 200)')
# 1158 function calls in 0.002 seconds
# 50 loops, best of 5: 244 usec per loop


# cProfile.run('pos_lst(100, 20000)')
# 115630 function calls in 0.063 seconds
# 50 loops, best of 5: 29.2 msec per loop






