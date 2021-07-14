"""
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк,
где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает его
среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.

Также вычислите средние баллы по математике,
физике и русскому языку по всем абитуриентам и добавьте полученные значения,
разделённые пробелом, последней строкой в файл с ответом.

В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной
строкой со средними оценками по трём предметам.

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
Sample Input:

Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85
Sample Output:

85.0
94.0
71.666666667
81.0 84.0 85.666666667
У вас есть неограниченное число попыток.
Время одной попытки: 5 mins
"""


def midl_rating(s):
    d = dict()
    mid_d = dict()
    les_1, les_2, les_3 = 0, 0, 0
    cnt = 0

    with open(s) as f:
        data = f.read().split()

    for el in data:
        el = el.split(';')
        d[el[0]] = el[1:]

    for key, value in d.items():
        mid_d[key] = round((int(value[0]) + int(value[1]) + int(value[2])) / 3, 9)
        cnt += 1
        les_1 += (int(value[0]))
        les_2 += (int(value[1]))
        les_3 += (int(value[2]))

    les_1, les_2, les_3 = round(les_1 / cnt, 9), round(les_2 / cnt, 9), round(les_3 / cnt, 9)

    with open(s + '.txt', 'w') as n:
        for key, value in mid_d.items():
            n.write(str(value) + '\n')
        n.write(f'{les_1} {les_2} {les_3}')


s = 'dataset_3363_4.txt'
midl_rating(s)

# Brown;50;84;57
