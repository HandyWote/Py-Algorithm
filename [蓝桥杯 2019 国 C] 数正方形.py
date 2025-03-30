n = int(input())
n -= 1
mod = 10**9 + 7
ans = 0
for i in range(1, n + 1):
    ans = (ans + (n - i + 1)**2 * i) % mod
print(ans)