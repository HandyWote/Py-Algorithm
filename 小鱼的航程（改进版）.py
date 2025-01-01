x,n = map(int,input().split())
s = 0
for i in range(n):
    if x > 7:
        x -= 7
    if x != 6 and x!= 7:
        s += 250
    x += 1
print(s)