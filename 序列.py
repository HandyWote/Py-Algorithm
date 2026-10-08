n,k = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
for i in range(n):
    for j in range(i+1,n):
        if a[i] * a[j] <= k:
            ans += 1
print(ans)