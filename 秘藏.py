n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
inf = -1<<60
dp = [[inf, inf] for _ in range(n)]
dp[0][0] = a[0]
dp[0][1] = inf
for i in range(1,n):
    dp[i][0] = max(dp[i-1][0]+a[i], dp[i-1][1]+a[i]-k if dp[i-1][1]>=k else inf)
    dp[i][1] = max(dp[i-1][0]+b[i]-k if dp[i-1][0]>=k else inf, dp[i-1][1]+b[i])
print(max(dp[-1]))