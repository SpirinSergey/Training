"""
Напишите функцию longest_word_in_file, которая принимает имя файла и внутри его содержимого находит самое
длинное слово и возвращает его в качестве ответа. В случае,  если есть несколько слов с максимальной длиной,
нужно вернуть слово, которое встречается последнее в тексте.

При этом слова в тексте отделяются друг от друга пробелами, любые другие знаки пунктуации необходимо исключить.
И также учитывайте, что слова в тестах будут как на русском языке, так и на английском

Все возможные знаки пунктуации можно получить из модуля string

from string import punctuation
"""


def longest_word_in_file(file_name):
    from string import punctuation
    str_line = ''
    data_list = []
    max_str = ''

    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.read()
        for el in data:
            if el in punctuation:
                str_line += " "
            else:
                str_line += el

    data_list = str_line.lower().split()

    for e in data_list:
        if len(e) >= len(max_str):
            max_str = e

    return max_str



longest_word_in_file('text.txt')
print('- - - - - - - - - - - - - - -')
longest_word_in_file('range_3.txt')


