# Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.

from random import randint, uniform


print('Варианты генерации:\n'
      '1 - Случайное целое число\n'
      '2 - Случайное вещественное число\n'
      '3 - Случайная буква алфавита\n')

change = input('Введите соответствующую цифру (от 1 до 3): \n')

if change == '1':
    print('Введите диапазон генерации:')
    num_1 = int(input('От - '))
    num_2 = int(input('До - '))
    print(randint(num_1, num_2))

elif change == '2':
    print('Введите диапазон генерации:')
    num_1 = float(input('От - '))
    num_2 = float(input('До - '))
    print(round(uniform(num_1, num_2), 5))

elif change == '3':
    print('Введите диапазон генерации (a - z):')
    alf_1 = ord(input('От - '))
    alf_2 = ord(input('До - '))
    print(chr(randint(alf_1, alf_2)))

else:
    print('Ошибка выбора!')

