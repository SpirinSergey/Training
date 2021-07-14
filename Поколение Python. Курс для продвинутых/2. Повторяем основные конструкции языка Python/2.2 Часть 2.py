"""
Координатные четверти
Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество точек,
лежащих в каждой координатной четверти.

Формат входных данных
В первой строке записано количество точек. Каждая следующая строка состоит из двух целых чисел — координат точки
(сначала абсцисса – xx, затем ордината – yy), разделенных символом пробела.

Формат выходных данных
Программа должна вывести количество точек, лежащих в каждой координатной четверти, как в примерах.

Примечание. Учтите, что точки, лежащие на осях координат, не принято относить к какой либо координатной четверти.

Sample Input 1:

4
0 -1
1 2
0 9
-9 -5
Sample Output 1:

Первая четверть: 1
Вторая четверть: 0
Третья четверть: 1
Четвертая четверть: 0
Sample Input 2:

10
4 8
-3 -1
-4 9
4 0
-4 0
5 -2
0 0
1 1
13 -3
-43 3
Sample Output 2:

Первая четверть: 2
Вторая четверть: 2
Третья четверть: 1
Четвертая четверть: 2
Напишите программу. Тес
"""

# n = int(input())
# coordinate_dict = {'Первая четверть:': 0,
#                    'Вторая четверть:': 0,
#                    'Третья четверть:': 0,
#                    'Четвертая четверть:': 0}
#
# for i in range(n):
#     s = list(map(int, input().split()))
#     if s[0] > 0 and s[1] > 0:
#         coordinate_dict['Первая четверть:'] += 1
#     elif s[0] < 0 and s[1] > 0:
#         coordinate_dict['Вторая четверть:'] += 1
#     elif s[0] < 0 and s[1] < 0:
#         coordinate_dict['Третья четверть:'] += 1
#     elif s[0] > 0 and s[1] < 0:
#         coordinate_dict['Четвертая четверть:'] += 1
#
# for key, value in coordinate_dict.items():
#     print(key, value)


# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

"""
Больше предыдущего
На вход программе подается строка текста, содержащая натуральные числа. 
Из данной строки формируется список чисел. Напишите программу, 
которая подсчитывает количество элементов полученного списка, больших предыдущего (элемента с предыдущим номером).

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.

Формат выходных данных
Программа должна вывести одно число – количество элементов списка, больших предыдущего.

Sample Input 1:

1 2 3 4 5
Sample Output 1:

4
Sample Input 2:

1 1 3 1 1
Sample Output 2:

1
Sample Input 3:

5 4 3 2 1
Sample Output 3:

0
"""

# def more_previous(s):
#     nums = list(map(int, s.split()))
#     cnt = 0
#     for i in range(len(nums) - 1):
#         if nums[i] < nums[i + 1]:
#             cnt += 1
#     print(cnt)
#
#
# s = input()
# more_previous(s)


# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

"""
Назад, вперёд и наоборот
На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел. 
Напишите программу, которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.). 
Если в списке нечетное количество элементов, то последний остается на своем месте.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.

Формат выходных данных
Программа должна вывести измененный список, разделяя его элементы одним пробелом.

Sample Input 1:

1 2 3 4 5
Sample Output 1:

2 1 4 3 5
Sample Input 2:

2 3 2 4
Sample Output 2:

3 2 4 2
Sample Input 3:

1
Sample Output 3:

1
"""

# def vice_versa(string):
#     num_list = [int(el) for el in string.split()]
#     if len(num_list) % 2 == 0:
#         for i in range(0, len(num_list), 2):
#             num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
#     elif len(num_list) % 2 == 1:
#         for i in range(0, len(num_list) - 1, 2):
#             num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
#     print(*num_list)
#
#
# s = input()
# vice_versa(s)


# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

"""
Сдвиг в развитии
На вход программе подается строка текста, содержащая натуральные числа. Из строки формируется список чисел. 
Напишите программу циклического сдвига элементов списка направо: каждый из элементов сдвинуть на одну позицию вперед, 
а последний поставить первым.

Формат входных данных
На вход программе подается строка текста, состоящая из натуральных чисел, разделенных пробелами.

Формат выходных данных
Программа должна вывести измененный список с циклическим сдвигом.

Sample Input 1:

1 2 3 4 5
Sample Output 1:

5 1 2 3 4
Sample Input 2:

0 0 0 0 0 0 0
Sample Output 2:

0 0 0 0 0 0 0
Sample Input 3:

5 4 3 2 1
Sample Output 3:

1 5 4 3 2
"""

# def shift(string):
#     num_list = string.split()
#     rev_list = num_list[-2::-1] + [num_list[-1]]
#     rev_list.reverse()
#     print(*rev_list)
#
#
# s = input()
# shift(s)


# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

"""
Различные элементы
На вход программе подается строка текста, содержащая натуральные числа, расположенные по неубыванию. 
Из строки формируется список чисел. Напишите программу для подсчета количества разных элементов в списке.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные символом пробела, 
расположенные по неубыванию.

Формат выходных данных
Программа должна вывести одно число – количество различных элементов списка.

Примечание. Задачу можно решить без использования дополнительной памяти (без списка, множества).
"""

# def various_elements(string):
#     num_list = string.split()
#     num = ''
#     cnt = 0
#     for el in num_list:
#         if el != num:
#             cnt += 1
#             num = el
#     print(cnt)
#
#
# s = input()
# various_elements(s)


# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

"""
Произведение чисел
Напишите программу для определения, является ли число произведением двух чисел из данного набора, 
выводящую результат в виде ответа «ДА» или «НЕТ».

Формат входных данных
В первой строке подаётся число n\\, (0 < n < 1000)n(0<n<1000) – количество чисел в наборе. 
В последующих nn строках вводятся целые числа, составляющие набор (могут повторяться). Затем следует целое число, 
которое является или не является произведением двух каких-то чисел из набора.

Формат выходных данных
Программа должна вывести «ДА» или «НЕТ» в соответствии с условием задачи.

Примечание. Само на себя число из набора умножиться не может, другими словами, 
два множителя должны иметь разные номера в наборе.
"""

# n = int(input())
# list_num = [int(input()) for el in range(n)]
# total_num = int(input())
# flag = False
#
# if len(list_num) > 1:
#
#     for el in list_num:
#         if el == 0:
#             continue
#         if (total_num // el) in list_num:
#             flag = True
#             if (total_num // el) == el and list_num.count(el) == 1:
#                 flag = False
#
# else:
#     flag = False
#
#
# print('ДА' if flag else 'НЕТ')


# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

"""
 Камень, ножницы, бумага
Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов". 
Для этого они решили сыграть в камень, ножницы и бумагу. Помогите ребятам бросить честный жребий и определить, 
кто будет делать очередной модуль нового курса.

Формат входных данных
На вход программе подаются две строки текста, содержащие слова "камень", "ножницы" или "бумага". 
На первой строке записан выбор Тимура, на второй – выбор Руслана.

Формат выходных данных
Программа должна вывести результат жеребьёвки, то есть кто победит Тимур, Руслан или они сыграют вничью.

Примечание. Правила игры стандартные: камень побеждает ножницы, но проигрывает бумаге, а ножницы побеждают бумагу.
"""

# def stone_paper_scissors(player_1, player_2):
#     game_dict = {'камень': ['ножницы', 'бумага'],
#                  'бумага': ['камень', 'ножницы'],
#                  'ножницы': ['бумага', 'камень']
#                  }
#     if game_dict[player_1][0] == player_2:
#         print('Тимур')
#     elif game_dict[player_1][1] == player_2:
#         print('Руслан')
#     else:
#         print('ничья')
#
#
# p_1, p_2 = input(), input()
# stone_paper_scissors(p_1, p_2)


# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

"""
Орел и решка
Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

Формат входных данных
На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

Формат выходных данных
Программа должна вывести наибольшее количество подряд выпавших Решек.

Примечание. Если выпавших Решек нет, то необходимо вывести число 00.

Sample Input 1:

ОРРОРОРООРРРО
Sample Output 1:

3
Sample Input 2:

ООООООРРРОРОРРРРРРР
Sample Output 2:

7
Sample Input 3:

ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР
Sample Output 3:

31
"""

# def heads_and_tails(string):
#     max_p = []
#     cnt = 0
#     for el in string:
#         if el == 'Р':
#             cnt += 1
#         elif el == 'О':
#             max_p.append(cnt)
#             cnt = 0
#     max_p.append(cnt)
#     print(max(max_p))
#
#
# s = input()
# heads_and_tails(s)


# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

"""
Кремниевая долина 🌶️
Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. 
Теперь он использует их в качестве серверов "Пегого дудочника". 
Помогите владельцу фирмы отыскать все зараженные холодильники.

Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, 
и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, 
главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, 
нумерация начинается с единицы

Формат входных данных
В первой строке подаётся число nn – количество холодильников. В последующих nn строках вводятся строки, 
содержащие латинские строчные буквы и цифры, в каждой строке от 55 до 100100 символов.

Формат выходных данных
Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, 
ничего выводить не нужно.
"""

# def anton_search(string):
#     ant_list = ['a', 'n', 't', 'o', 'n']
#     infected = []
#     for i in range(1, string + 1):
#         for el in input():
#             if ant_list[0] == el:
#                 del ant_list[0]
#             if len(ant_list) == 0:
#                 infected.append(i)
#                 break
#         ant_list = ['a', 'n', 't', 'o', 'n']
#     if len(infected) > 0:
#         print(*infected)
#
#
# n = int(input())
# anton_search(n)


# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

"""
Роскомнадзор запретил букву а 🌶️🌶️
Необходимо написать программу, реализующую алгоритм написания этой песни. Алгоритм выводит в конце предложения следующую в алфавитном порядке букву, если она встречается в строке текста, а очередную строку отображает уже без этой буквы.

Формат входных данных
На вход программе подается одно слово, записанное строчными русскими буквами без буквы "ё".

Формат выходных данных
Программа должна вывести в соответствии с указанным алгоритмом строки, количество которых равно количеству разных букв в строке, которая получается путем конкатенации введенного слова и строки "запретил букву".

Примечание 1. Текст исходной песни в первом тесте.

Примечание 2. Поем и решаем друзья, поем и решаем 😂.

Made with 💛 by Anri Tabuev
Sample Input 1:

роскомнадзор
Sample Output 1:

роскомнадзор запретил букву а
роскомндзор зпретил букву б
роскомндзор зпретил укву в
роскомндзор зпретил уку д
роскомнзор зпретил уку е
роскомнзор зпртил уку з
роскомнор пртил уку и
роскомнор пртл уку к
росомнор пртл уу л
росомнор прт уу м
росонор прт уу н
росоор прт уу о
рср прт уу п
рср рт уу р
с т уу с
т уу т
уу у
Sample Input 2:

тимур
Sample Output 2:

тимур запретил букву а
тимур зпретил букву б
тимур зпретил укву в
тимур зпретил уку е
тимур зпртил уку з
тимур пртил уку и
тмур пртл уку к
тмур пртл уу л
тмур прт уу м
тур прт уу п
тур рт уу р
ту т уу т
у уу у
"""

# word = input() + ' запретил букву'
# alp_wrd = sorted(list(set(word)))
#
# for i in range(1, len(alp_wrd)):
#     if '  ' in word:
#         word = word.replace('  ', ' ')
#     word = word.strip()
#     print(word, alp_wrd[i])
#     for el in word:
#         if el == alp_wrd[i]:
#             word = word.replace(alp_wrd[i], '')


# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

"""
Камень, ножницы, бумага, ящерица, Спок 🌶️
Проиграв 1010 раз Тимуру, Руслан понял, что так дело дальше не пойдет, и решил усложнить игру. 
Теперь Тимур и Руслан играют в игру Камень, ножницы, бумага, ящерица, Спок. 
Помогите ребятам вновь бросить честный жребий и определить, кто будет делать следующий модуль в новом курсе.

Формат входных данных
На вход программе подаются две строки текста, содержащие по одному слову из перечня "камень", "ножницы", "бумага", 
"ящерица" или "Спок". На первой строке записан выбор Тимура, на второй – выбор Руслана.

Формат выходных данных
Программа должна вывести результат жеребьёвки: кто победил - Тимур или Руслан, или они сыграли вничью.

Примечание. Правила игры стандартные: ножницы режут бумагу. Бумага заворачивает камень. Камень давит ящерицу, 
а ящерица травит Спока, в то время как Спок ломает ножницы, которые, в свою очередь, отрезают голову ящерице, 
которая ест бумагу, на которой улики против Спока. Спок испаряет камень, а камень, разумеется, затупляет ножницы.
"""

def stone_paper_scissors(player_1, player_2):
    d = {
        'камень': ['ножницы', 'ящерица', 'бумага', 'Спок'],
        'ножницы': ['бумага', 'ящерица', 'камень', 'Спок'],
        'бумага': ['камень', 'Спок', 'ножницы', 'ящерица'],
        'ящерица': ['бумага', 'Спок', 'камень', 'ножницы'],
        'Спок': ['камень', 'ножницы', 'бумага', 'ящерица']
    }

    if d[player_1][0] == player_2 or d[player_1][1] == player_2:
        print('Тимур')
    elif d[player_1][2] == player_2 or d[player_1][3] == player_2:
        print('Руслан')
    else:
        print('ничья')


p_1, p_2 = input(), input()
stone_paper_scissors(p_1, p_2)


# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _The end _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
