import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = list(map(int, input().split()))

# 树状数组
bit = [0] * (n + 2)

def update(i):
    while i <= n:
        bit[i] += 1
        i += i & -i

def query(i):
    s = 0
    while i:
        s += bit[i]
        i -= i & -i
    return s

opt = 0
for i in range(n):
    opt += i - query(p[i])
    update(p[i])

# 找最小的 >= opt 且奇偶相同的 M 倍数
t = ((opt + m - 1) // m) * m
if (t - opt) % 2 == 0:
    print(t)
elif m % 2 == 1:
    print(t + m)
else:
    print(-1)
