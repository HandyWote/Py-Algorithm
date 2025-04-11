ans = 0
for i in range(1,2025):
    b = list(str(bin(i)))
    b = b[2::]
    sb = sum(map(int, b))
    sf = 0
    f = i
    c = 0
    while f >= 4:
        c = f % 4
        sf += c
        f = (f-c) / 4
    sf += f
    if sb == sf:
        ans += 1
print(ans)