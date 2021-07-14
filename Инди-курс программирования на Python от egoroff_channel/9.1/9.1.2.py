"""
Напишите функцию create_file_with_numbers, которая принимает на вход одно целое положительное число - n.

Функция должна создать файл с название "range_<number>.txt" и наполнить его целыми числами от 1 до n включительно,
причем каждое число записывается  в отдельной строке

Пример: функция create_file_with_numbers(5) должна создать файл "range_5.txt" с содержимым
"""


def create_file_with_numbers(n):
    file_name = 'range_' + str(n) + '.xml'
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, n + 1):
            f.write(str(i) + '\n')


create_file_with_numbers(5)
create_file_with_numbers(4)
create_file_with_numbers(3)