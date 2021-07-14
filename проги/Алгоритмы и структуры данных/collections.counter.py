from collections import Counter
from icecream import ic

a = Counter()
b = Counter('Hello')
c = Counter({'red': 2, 'blue': 4})
d = Counter(cats=4, dogs=5)

print(a, b, c, d, sep='\n')