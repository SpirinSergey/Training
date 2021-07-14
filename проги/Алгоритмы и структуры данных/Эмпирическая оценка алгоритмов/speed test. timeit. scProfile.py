import timeit

import cProfile


print(timeit.timeit('[el * 10 - 5 for el in range(1, 90)]'))



cProfile.run('')
