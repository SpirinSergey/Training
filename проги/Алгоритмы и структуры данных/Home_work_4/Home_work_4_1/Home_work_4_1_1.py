import cProfile
from random import randint


def pos_lst(range_num, len_list):
    new_list = []
    start_list = [randint(1, range_num) for i in range(len_list)]
    for i, el in enumerate(start_list):
        if el % 2 == 0:
            new_list.append(i)
    return new_list


# pos_lst(100, 20)

# cProfile.run('pos_lst(100, 20)')
# 119 function calls in 0.001 seconds
# 50 loops, best of 5: 27.7 usec per loop


# cProfile.run('pos_lst(100, 200)')
# 1170 function calls in 0.001 seconds
# 50 loops, best of 5: 251 usec per loop


# cProfile.run('pos_lst(100, 20000)')
# 115619 function calls in 0.069 seconds
# 50 loops, best of 5: 27.4 msec per loop



