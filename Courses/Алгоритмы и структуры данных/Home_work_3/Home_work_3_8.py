# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу. +

matrix = [[], [], [], []]
total = 0

for i in range(4):
    total = 0
    for j in range(4):
        num = int(input(f'Введите {j + 1} - элемент {i + 1} - строки: '))
        matrix[i].append(num)
        total += num
    matrix[i].append(" | " + str(total))

print()

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
