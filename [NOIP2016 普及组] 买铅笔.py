import math
a = []
n = int(input())
for i in range(3):
    b,c = map(int,input().split())
    a.append(math.ceil(n/b) * c)
print(min(a))