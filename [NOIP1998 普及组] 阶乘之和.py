n = int(input())
s = 0
for i in range(1, n+1):
    s1 = 1
    for j in range(1, i+1):
        s1 *= j
    s += s1
print(s)