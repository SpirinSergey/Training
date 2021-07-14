def stringy(size):
    bin_list = ['1', '0']
    result = ''
    for i in range(size):
        for j in range(2):
            if i % 2 == 0:
                result += bin_list[j]
    return result


print(stringy(1))
print(stringy(2))
print(stringy(3))
print(stringy(5))
print(stringy(10))

