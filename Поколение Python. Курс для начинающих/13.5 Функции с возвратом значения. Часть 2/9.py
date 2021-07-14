"""
Змеиный регистр
Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в
«верблюжьем регистре» и преобразует его в «змеиный регистр».

Примечание 1. Почитать подробнее о стилях именования можно тут.

Примечание 2. Следующий программный код:

print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))
должен выводить:

this_is_camel_cased
is_prime_number
"""


# объявление функции
def convert_to_python_case(text):
    new_text = []
    z = 0
    for el in text:
        if el.isupper():
            z += 1
            if z > 0:
                new_text.append('_')
                new_text.append(el.lower())
        else:
            new_text.append(el)
    return ''.join(new_text[1:])


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
