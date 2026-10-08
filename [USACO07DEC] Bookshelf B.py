n,h = map(int,input().split())
a = []
ans = 0
count = 1
for i in range(n):
    a.append(int(input()))
a.sort()
a = a[::-1]
for i in range(n):
    ans += a[i]
    if h > ans:
        count += 1
    else:
        print(count)
        break