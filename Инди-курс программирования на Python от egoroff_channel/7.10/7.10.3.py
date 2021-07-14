"""
В python есть стандартный модуль datetime.

Внутри него имеется функция datetime.datetime.now() при помощи которой, можно найти текущую дату в формате (год, месяц,
день, час, минуты, секунды, млсекунды)

Ваша задача написать три lambda функция, которые принимают текущую дату и возвращают год, месяц и день соответственно.

Эти три lambda функции нужно будет сохранить в переменные get_year, get_month и get_day соответственно.

Вызывать ничего не нужно, просто создайте функции
"""

import datetime

now = datetime.datetime.now()

get_year = lambda x: x.year
get_month = lambda x: x.month
get_day = lambda x: x.day

print(get_year(now))
print(get_month(now))
print(get_day(now))
