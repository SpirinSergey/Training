"""
Напишите программу, которая выводит все цифры, встречающиеся в символьной строке больше одного раза.

Входные данные
Входная строка может содержать содержит цифры, пробелы и латинские буквы.

Выходные данные
Программа должна вывести в одну строчку в порядке возрастания все цифры,
встречающиеся во входной строке больше одного раза. Если таких цифр нет, нужно вывести слово 'NO'.

Sample Input 1:

abc12cd34ef35
Sample Output 1:

3
Sample Input 2:

yrey424u3iou2315
Sample Output 2:

2 3 4
Sample Input 3:

qwerty123
Sample Output 3:

NO
"""

s = input()
num_set = sorted(set([el for el in s if el.isdigit() and s.count(el) >= 2]))
print('NO' if len(num_set) == 0 else ' '.join(num_set))

