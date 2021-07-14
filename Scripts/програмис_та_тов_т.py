
def programmers(num):
    if num % 10 in [0, 5, 6, 7, 8, 9] or num % 100 in [11, 12, 13, 14]:
        print(num, 'программистов')
    elif num % 10 == 1 or num % 100 in [31, 51, 71, 91]:
        print(num, 'программист')
    else:
        print(num, 'программиста')


programmers(1)
programmers(10)
programmers(35)
