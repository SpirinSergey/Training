"""Напишите программу, которая печатает словарь alphabet, где ключи  - строчные английские символы,
а значения - порядковые номера букв в алфавите.
Начало вашего словаря должны быть таким {"a": 1, "b": 2 }
В качестве ответа распечатайте ключи и значения данного словаря по алфавиту, каждую пару на новой строчке.
Весь английский алфавит можно взять в переменной ascii_lowercase из модуля string:
from string import ascii_lowercase
print(ascii_lowercase)"""

from string import ascii_lowercase

alphabet = {ascii_lowercase[i]: i + 1 for i in range(len(ascii_lowercase))}

for key, value in alphabet.items():
    print(key, value)
