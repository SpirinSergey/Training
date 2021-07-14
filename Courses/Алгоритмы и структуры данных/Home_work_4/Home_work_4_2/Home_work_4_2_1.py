import cProfile

def era(n):
    s = n
    n = n * 30
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):

        if sieve[i] != 0:
            j = i * 2

            while j < n:
                sieve[j] = 0
                j += i

    result = [i for i in sieve if i != 0]

    return result[s - 1]


# print(era(2000))


# cProfile.run('era(2)')
# 6 function calls in 0.000 seconds
# 1000 loops, best of 5: 18.3 usec per loop


# cProfile.run('era(200)')
# 6 function calls in 0.030 seconds
# 1000 loops, best of 5: 2.42 msec per loop


# cProfile.run('era(2000)')
# 6 function calls in 0.378 seconds
# 1000 loops, best of 5: 28 msec per loop



