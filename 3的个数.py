a,b = map(str,input().split())
n = 0
for i in range (len(a)):
    if int(a[i]) == 3:
        n += 1
if n == int(b):
    print('YES')
else:
    print('NO')