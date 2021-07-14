n, m = map(int, input().split())
s = []

list_g = []
list_v = []

for i in range(n):
    s.append(map(int, input().split()))

for a in range(n):
    for b in range(m):
    total_g += s[n][m]
        if b == m - 1:
            list_g.append(total_g)

for c in range(m):
    total_v = 0
    for v in range(n):
        total_v += s[m][n]
        if v == n - 1:
            list_g.append(total_v)

print(total_g)
print(total_v)


