"""
Правильная скобочная последовательность
Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text,
состоящую из символов ( и ) и возвращает значение True если поступившая на вход строка является
правильной скобочной последовательностью и False в противном случае.

Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только из символов ( и ),
где каждой открывающей скобке найдется парная закрывающая скобка.

Примечание 2. Следующий программный код:

print(is_correct_bracket('()(()())'))
print(is_correct_bracket(')(())('))
должен выводить:

True
False
"""


# объявление функции
def is_correct_bracket(text):
    t = 0
    for el in text:
        if el == '(':
            t += 1
        elif el == ')':
            t -= 1
            if t < 0:
                return False
    return True if t == 0 else False


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
