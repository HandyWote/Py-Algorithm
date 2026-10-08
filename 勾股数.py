import math
n = int(input())
s = []
for a in range(1,n):
    for b in range(a,n):
        c = math.ceil(math.sqrt(a**2+b**2))
        if c<=n and c**2 == a**2 + b**2:
            s.append(c)
print(int(len(s)))