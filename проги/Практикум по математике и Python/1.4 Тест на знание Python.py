# Список L содержит целые числа.
# Запишите в переменную index индекс элемента,
# разность между которым и следующим равна 1 (не важно какой из двух элементов больше).
# Гарантируется, что в списке есть ровно 1 такая пара.
# Темы: for
#
# Sample Input 1:
# 1 4 67 4 2 65 66
# Sample Output 1:
# 5
# Sample Input 2:
# 1 2 6
# Sample Output 2:
# 0
# Sample Input 3:
# 1 2
# Sample Output 3:
# 0

index = 0
for i in range(len(L) + 1):
    if L[i + 1] - L[i] == 1:
        index = i
        break