def expanded_form(num):
    resulte = []
    num = str(num).split(".")
    if int(num[0]) > 0:
        [resulte.append(num[0][i] + (len(num[0]) - i - 1) * '0') for i in range(len(num[0])) if int(num[0][i]) > 0]
    num_2 = str(num[1])
    [resulte.append(num_2[i] + '/1' + (i + 1) * '0') for i in range(len(num_2)) if int(num_2[i]) > 0]
    return ' + '.join(resulte)

