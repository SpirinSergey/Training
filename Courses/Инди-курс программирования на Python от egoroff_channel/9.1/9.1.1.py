"""
Напишите функцию file_read, которая принимает имя файла, и печатает его содержимое.

Учитывайте, что содержимое файла может быть как на русском языке, так и на английском
"""


def file_read(file_name):
    with open(file_name, encoding='utf-8') as f:
        data = f.read()
        print(data)


file_read('text.txt')

