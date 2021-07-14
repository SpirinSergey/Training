
def expanded_form(num):
    num = str(num)
    num_list = [num[i] + (len(num) - i - 1) * '0' for i in range(len(num)) if int(num[i]) > 0]
    return ' + '.join(num_list)


print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))
