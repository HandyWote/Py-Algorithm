def solve():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if i + n - k <= n:
            ans = max(ans,sum(a[i:i+n-k]))
    print(ans)
    return 0
solve()