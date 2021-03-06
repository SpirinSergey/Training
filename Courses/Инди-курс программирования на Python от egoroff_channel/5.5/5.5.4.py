

"""Все просто, вам поступает число n - количество элементов в списке, и затем сам список.
Ваша задача отсортировать список по возрастанию при помощи пузырьковой сортировки,
в случае если элементы соседние совпадают менять их ненужно.
В качестве ответа нужно вывести отсортированный список и какое количество раз пришлось
переставлять элементы в процессе сортировки"""


n, list_num = int(input()), list(map(int, input().split()))
count = 0

for i in range(n):
    for j in range(n - 1):
        if list_num[j] > list_num[j + 1]:
            list_num[j], list_num[j + 1] = list_num[j + 1], list_num[j]
            count += 1

print(*list_num)
print(count)