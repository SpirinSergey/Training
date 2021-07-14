import cProfile


def simple(n):
    s = n
    n = n * 30
    lst = [2]
    for i in range(3, n+1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst[s - 1]


# print(simple(2))


# cProfile.run('simple(2)')
# 112 function calls in 0.000 seconds
# 1000 loops, best of 5: 220 usec per loop


# cProfile.run('simple(200)')
# 6060 function calls in 0.066 seconds
# 1000 loops, best of 5: 3.58 msec per loop


# cProfile.run('simple(2000)')
# 49101 function calls in 1.298 seconds
# 1000 loops, best of 5: 63.5 msec per loop



