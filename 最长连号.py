n = int(input())
a = list(map(int, input().split()))
l = [a[0]]
ans = []
temp = 1
for i in range(1, n):
    l.append(a[i])
    if l[-1] == l[-2] + 1:
        temp += 1
    else:
        l = [a[i]]
        ans.append(temp)
        temp = 1
ans.append(temp)
print(max(ans))