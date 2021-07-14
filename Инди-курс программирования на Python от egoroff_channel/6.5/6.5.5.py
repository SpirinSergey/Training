"""
Дили Вили Били завели себе аккаунты в одной известной соцсети.
И затем они решили узнать у кого из них самое большое количество уникальных комментатор.
Ваша задача помочь им в этом и собрать нужную информацию.

Входные данные
В каждой строке будет вводиться одно из имен наших героев, а затем через двоеточие и пробел имя комментатора.
Комментаторы могут повторяться и комментировать разных персонажей

Строка "конец" означает окончание ввода и встречается последней

Входные данные
Ваша задача вывести в порядке уменьшения популярности 3 строки вида:
"Количество уникальных комментаторов у <имя героя> - <количество комментаторов>"
На склонение давайте не будем обращать обращать внимания в этой задаче.

Гарантируется, что количество уникальных комментаторов у всех наших героев разное.
Могут быть ситуации, когда у героя нету ни единого комментатора,
в таком случае все равно нужно выводить информацию о нем.
"""

dli, vli, bli = set(), set(), set()
s = []

while True:
    s = input()
    if s == 'конец':
        break
    else:
        s = s.split(': ')
        if s[0] == 'Дили':
            dli.update({s[1]})
        if s[0] == 'Вили':
            vli.update({s[1]})
        if s[0] == 'Били':
            bli.update({s[1]})

dict_name = {}

dict_dli = {'Количество уникальных комментаторов у Дили -': len(dli)}
dict_vli = {'Количество уникальных комментаторов у Били -': len(bli)}
dict_bli = {'Количество уникальных комментаторов у Вили -': len(vli)}

dict_name.update(dict_dli)
dict_name.update(dict_vli)
dict_name.update(dict_bli)

for key, value in sorted(dict_name.items(), key=lambda para: para[1], reverse=True):
    print(key, value)
