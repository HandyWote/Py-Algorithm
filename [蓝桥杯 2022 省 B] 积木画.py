n = int(input())
mod = 1e9+7
f = [0, 1, 2, 5] + [0]*(n-2)
for i in range(4,n+1):
    f[i] = (2*f[i-1]%mod + f[i-3]%mod)%mod
print(f[n])