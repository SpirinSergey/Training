"""
Вам дан список numbers, в нем есть и отрицательные числа и нули и положительные значения. Гарантируется,
что список целиком состоит только из чисел.

Необходимо при помощи функций filter и len определить сколько в этом списке отрицательных значений,
сколько нулей и сколько положительных. Вывести найденные значения в том же порядке
"""

numbers = [54, 71, 65, 51, 36, -82, -32, 61, -61, 92, 17, -68, -62, 40, 16, -49, -51, -38, 60, -24, -61, 3, -26, -46,
           -97, -28, 36, 7, 52, 56, -96, -69, 67, 76, 16, 36, 38, 74, 11, -87, 69, 69, -69, -61, 92, 67, -45, -26, 94,
           38, 27, -26, 10, 55, 28, -81, 53, -75, -32, -83, 38, 83, -40, -51, 88, 28, 76, 25, 84, -79, -69, -65, 6, 12,
           81, -58, -92, 44, -41, 60, -14, -65, 7, 64, -40, -25, -91, -23, -19, -40, -4, 36, 38, 28, -27, -28, 72, 47,
           -95, 47, 10, 31, 62, -75, 22, -34, 44, -62, -30, -41, 19, -13, 30, -11, -54, -46, -80, -57, -60, 72, -49,
           84, 5, 66, 62, -35, 69, 23, 41, -15, 75, -53, 94, -76, -28, -41, -17, 71, 67, -50, 18, 65, -16, -27, -88,
           21, -42, 58, 85, 36, 9, -72, -26, -73, -1, 41, -87, 85, 5, -92, -60, -33, 33, -74, 17, 47, -38, -95, -39,
           64, 85, -27, -42, -91, -39, -15, -75, 78, -54, 26, -10, -3, 89, -11, -71, -85, 63, 9, -59, 72, 27, 40, 99,
           -9, 77, 64, -39, -28, 73, -50, -80, -74, 52, 26, 53, -18, 22, 70, 85, 1, -90, 53, -19, -80, -14, -29, -64,
           -21, 23, 99, 15, -52, 66, 30, 82, -81, -30, -68, 30, -25, -63, 33, 1, 0, 84, 18, -35, 31, -34, 10, 48, -37,
           -41, -94, -1, -14, -87, -37, -6, 48, 38, 33, -13, 71, -81, 45, -63, 52, -35, 34, -88, -82, -7, -92, -22,
           96, -28, 0, 21, 74, -28, 81, 81, 44, -16, 17, -95, 18, -73, 15, -61, 6, -43, -67, -31, -61, -72, -66, 60,
           67, -13, 47, 29, 44, -93, 55, -13, -23, 74, 79, 32, -20, 33, 17, -48, 7, 24, 19, 89, -60, 34, 81, 18, -39,
           56, 10, -32, 46, -33, -75, -99, -37, -23, 59, -33, -1, 75, -65, 92, 80, 51, -59, -28, -22, -47, -1, 28,
           -85, 1, 23, -15, -66, -97, -25, 7, 17, -87, -60, 14, -70, 88, 20, 40, -89, 38, -41, -97, 76, 80, 43, 22,
           -72, -38, 47, -2, 12, 58, -91, 82, -98, 50, 15, -33, -56, 69, -27, 94, -90, 92, -71, -73, -71, -78, 22,
           -86, -48, 10, 46, 19, 68, -23, 52, -42, 74, 44, 89, -71, 93, 43, -86, 79, 3, -56, 14, 41, 15, -37, 77, -9,
           36, 51, -89, 1, 37, 82, 27, 72, -92, 91, 94, 71, -81, -49, -42, 26, 57, -30, -40, 86, -77, -85, 1, 71, 16,
           73, -82, 26, -90, 72, 14, -65, -55, 34, 45, 66, -64, -40, 92, 42, -78, -22, 53, -18, -41, -75, 10, -59,
           -55, 8, -90, -3, -65, 43, -49, -86, -96, 69, 48, 27, -48, -42, -34, -6, 7, 50, -55, -65, 79, 30, 16, -21,
           -98, -73, -25, -20, -51, 20, 17, -91, 34, 96, 12, 13, -58, -73, -82, 19, -48, -61, 57, 96, 74, 34, -63, 38,
           -27, -12, -24, 94, -25, -10, -41, 53, -13, 16, -21, 24, 96, 95, 58, 83, 10, 42, -11, -33, 10, 38, -6, -66,
           -40, -36, -99, -55, 37, -81, -93, 67, -77, -3, 77, 25, 38, -16, 21, -82, 77, 95, 73, 9, 94, -27, -21, -33,
           -90, 31, 98, 28, -63, 75, 53, -17, -1, 6, 51, 11, -92, 30, -24, 12, 47, -75, -15, -63, 57, 3, 37, -82, -28,
           -26, -3, -30, -90, -45, 20, -41, 72, -42, 15, -3, 92, 57, -1, 40, -65, 88, 28, -76, 52, -63, -51, 59, 69,
           -39, -47, -1, -18, -57, 68, 77, 66, 62, -71, 31, -50, 61, 88, 98, 5, 98, -57, -46, 2, 90, 43, 67, 76, -81,
           -57, 77, 25, -66, -81, -92, -76, 72, 14, 59, 52, 36, 20, -2, 92, 58, 36, -34, 94, -74, 42, -56, 96, -81,
           69, -83, 71, -13, -13, 56, 86, -29, 58, -17, 65, 70, 74, 28, 8, 91, 51, 79, -57, -86, 5, -37, -67, -28, 56,
           65, -90, 97, -20, 81, -85, -45, 46, -74, 76, -75, -7, 74, 82, 56, 14, -43, 20, -48, -99, 19, -39, -66, 44,
           -75, 24, -5, -70, 85, -12, 20, -85, -69, -26, -57, 28, -96, 42, -56, 13, 80, -48, 59, 11, -30, 4, -96, 58,
           41, -2, -84, -51, 52, -69, 37, 60, -12, 48, -5, -48, 29, -62, 42, 15, 16, 65, 60, 43, -53, 4, 50, -21, 1,
           -21, -42, -57, -21, -50, -67, 77, -22, -5, 59, -67, 86, -77, 39, -67, 41, 83, -21, 33, 73, 55, 80, 93, 44,
           -71, 38, -93, 4, 83, -52, 75, -51, 1, -11, -45, 56, 81, 84, 70, 23, -36, -63, 69, 1, 86, -21, 53, -85, 70,
           -89, -31, -10, -94, -76, -17, -21, -60, 49, -22, -48, 67, 21, 18, 89, 20, 73, -43, -17, -52, 36, -21, 6,
           -37, -98, 94, 56, 31, 99, 86, 65, -19, -67, 46, 20, -29, -88, -54, 88, -12, -69, 17, 83, -94, 21, 59, -99,
           70, -54, -35, 2, 58, 93, 1, -35, -44, 47, 40, 55, 10, -15, -96, -42, 10, -83, -82, -26, 48, 78, -72, 56,
           -99, -36, 25, 76, -3, -95, -38, -24, 96, 82, 7, 84, 46, 8, 93, -52, -86, 87, -85, -81, 52, -67, 52, -45,
           -93, -69, 60, -83, -20, -14, 80, -36, 62, -78, 3, -61, 51, 48, 73, 92, -65, 71, -86, 8, -14, 82, 58, -58,
           -21, 62, -38, 16, 20, -80, -78, 19, 19, 93, -83, 2, 71, 85, 71, -4, 81, 4, 90, 73, 21, -3, -55, 49, 66,
           -4, -6, 42, 76, -3, -94, 49, 55, -53, 12, 1, -25, 56, 93, -68, -21, 15, -13, 35, 71, -68, 34, -44, 48, 97,
           51, 32, 87, 27, -85, -41, -27, 54, -91, -99, 83, -44, 70, -87, -76, 49, 99, 38, 15, 75, -54, -59, 22, 80,
           49, -63, 8, -46, 97, -4, -92, -47, -20]

up_zero = len(list(filter(lambda x: x < 0, numbers)))
zero = len(list(filter(lambda x: x == 0, numbers)))
down_zero = len(list(filter(lambda x: x > 0, numbers)))

print(up_zero, zero, down_zero)



