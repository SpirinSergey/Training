"""
Давайте начнем с легкого примера. Создадим функцию с именем keanu_reeves, которая выводит сообщение

"YOU'RE BREATHTAKING"
Ваша задача написать только определение функции
"""

#
# def keanu_reeves():
#     print("YOU'RE BREATHTAKING")

year = int(input())

while True:
    year += 1
    year_list = [int(e) for e in str(year)]
    year_set = set(year_list)
    if len(year_set) == 4:
        break

print(year)
