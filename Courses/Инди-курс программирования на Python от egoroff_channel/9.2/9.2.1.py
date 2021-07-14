"""
Анализ продаж
К вам в руки попал файлик формата json , в котором содержится информация одного автосалона о продажах менеджеров.
В файле указано для каждого менеджера список проданных им автомобилей,
а также проставлена цена продажи каждого автомобиля.

Ваша задача скачать файлик и самостоятельно найти имя и фамилию самого успешно менеджера,
а также общую сумму его продаж. В качестве ответа нужно через пробел указать сперва его имя,
затем фамилию и после общую сумму его продаж.
"""

import json

new_dic = dict()

with open('manager_sales.json', 'r') as f:
    data = json.load(f)

for el in data:
    lst = []
    for e in el['cars']:
        lst.append(e['price'])
    new_dic[el['manager']['first_name'] + ' ' + el['manager']['last_name']] = sum(lst)

for key, value in sorted(new_dic.items(), key=lambda para: para[1], reverse=True):
    print(key, value)

