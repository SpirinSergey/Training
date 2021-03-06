
"""Состязания
В метании молота состязается n спортcменов. Каждый из них сделал m бросков.
Победителем считается тот спортсмен, у которого сумма результатов по всем броскам максимальна.
Если перенумеровать спортсменов числами от 0 до n-1, а попытки каждого из них – от 0 до m-1,
то на вход программа получает массив A[n][m], состоящий из неотрицательных целых чисел.
Программа должна определить максимальную сумму чисел в одной строке и вывести на экран эту сумму и номер строки,
для которой достигается эта сумма.
Входные данные
Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве.
Далее во входном потоке идет n строк по m чисел, являющихся элементами массива.
Выходные данные
Программа должна вывести  2 числа: сумму и номер строки, для которой эта сумма достигается.
Если таких строк несколько, то выводится номер наименьшей из них.
Не забудьте, что нумерация строк (спортсменов) начинается с 0."""


n, m = map(int, input().split())
sport_list = []

for i in range(n):
    sport_list.append(sum([int(el) for el in input().split()]))

print(max(sport_list), sport_list.index(max(sport_list)), sep='\n')





