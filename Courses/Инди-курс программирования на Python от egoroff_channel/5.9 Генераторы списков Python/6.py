"""На вход программе подается натуральное число n (n<=1000).
При помощи list comprehension создайте список, состоящий из делителей введенного числа."""

n = int(input())
print([el for el in range(1, n + 1) if n % el == 0])