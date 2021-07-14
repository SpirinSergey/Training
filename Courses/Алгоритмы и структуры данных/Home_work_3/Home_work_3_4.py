# 4. Определить, какое число в массиве встречается чаще всего. +

from random import randint

new_list = []
size = 20

start_list = [randint(1, 10) for i in range(size)]
print(f'Массив случайных чисел - {start_list}')

num = start_list[0]
max_frq = 1

for i in range(size - 1):

    frq = 1
    for k in range(i + 1, size):

        if start_list[i] == start_list[k]:
            frq += 1

    if frq > max_frq:
        max_frq = frq
        num = start_list[i]

if max_frq > 1:
    print(max_frq, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')
