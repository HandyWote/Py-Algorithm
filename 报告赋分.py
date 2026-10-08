t = int(input())
ans = []
for _ in range(t):
    a, p = map(int, input().split())
    if p < 16:
        if a >= 10:
            ans.append(a - 10)
        else:
            ans.append(0)
    elif p > 20:
        if a > p - 20:
            ans.append(a - (p - 20))
        else:
            ans.append(0)
    else:
        ans.append(a)

for i in range(len(ans)):
    print(ans[i])