from random import randint

array = [randint(-100, 100) for _ in range(100)]
print(array)

arr_below = []
arr_lager = []

for item in array:

    if item > 0:
        arr_lager.append(item)
    elif item < 0:
        arr_below.append(item)

print()
print(arr_lager)

print()
print(arr_below)