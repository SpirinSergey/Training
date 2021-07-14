"""Функция Треугольник Паскаля"""


def triangle_pascal(n):
    n = int(input())
    triangle = [[1] + [0] * n for el in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1]
    return triangle


print(triangle_pascal(45))
