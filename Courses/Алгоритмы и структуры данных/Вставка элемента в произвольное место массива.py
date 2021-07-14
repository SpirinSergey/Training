from random import randint

array = [randint(-100, 100) for _ in range(100)]
print(array)

num = int(input('Введите целое число для вставки: '))
pos = int(input('На какую позицию вставить элемент: '))

array.append(None)
i = len(array) - 1
while i > pos:
    array[i], array[i - 1] = array[i - 1], array[i]
    i -= 1

# array.insert(pos,num)

array[pos] = num
print(array)
