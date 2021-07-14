import cProfile

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# test_fib(fib)

# cProfile.run('fib(10)')
# 180 function calls (4 primitive calls) in 0.000 seconds

# cProfile.run('fib(15)')
# 1976 function calls (4 primitive calls) in 0.001 seconds

# cProfile.run('fib(20)')
# 21894 function calls (4 primitive calls) in 0.009 seconds

# cProfile.run('fib(25)')
# 242788 function calls (4 primitive calls) in 0.101 seconds

# C:\Users\Сергей Игоревич\Desktop\development\Алгоритмы и структуры данных>python -m timeit -n 1000 -s "import task" "task.fib(10)"
# 1000 loops, best of 5: 27.1 usec per loop

# C:\Users\Сергей Игоревич\Desktop\development\Алгоритмы и структуры данных>python -m timeit -n 1000 -s "import task" "task.fib(15)"
# 1000 loops, best of 5: 297 usec per loop

# C:\Users\Сергей Игоревич\Desktop\development\Алгоритмы и структуры данных>python -m timeit -n 1000 -s "import task" "task.fib(20)"
# 1000 loops, best of 5: 3.32 msec per loop

# C:\Users\Сергей Игоревич\Desktop\development\Алгоритмы и структуры данных>python -m timeit -n 1000 -s "import task" "task.fib(25)"
# 1000 loops, best of 5: 38.9 msec per loop

# >python -m timeit -n 1000 -s "import Home_work_4_2_1" "Home_work_4_2_1.era(200)"





