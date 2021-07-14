"""
В json-файле содержится информация о нескольких групп людей, при этом у каждой группы есть свой идентификатор.

Ваша задача скачать файлик и самостоятельно найти идентификатор группы,
в которой находится самое большое количество женщин, рожденных после 1977 года.
В качестве ответа необходимо указать через пробел идентификатор найденной группы и сколько в ней было женщин,
рожденных после 1977 года.
"""
import json

lst = []
dict_list = dict()

with open('group_people.json') as f:
    data = json.load(f)

for el in data:
    cnt = 0
    for elem in el['people']:
        if elem['gender'] == 'Female' and elem['year'] > 1977:
            cnt += 1
    dict_list[el['id_group']] = cnt


for key, value in sorted(dict_list.items(), key=lambda para: para[1], reverse=True):
    print(key, value)
