n, v, m, a = map(int, input().split())
money = 0
for i in range(n):
    money += v
    if (i + 1) % m == 0:
        v += a
print(money)