from functools import cache

MX = 201
divisors: list[list[int]] = [[] for _ in range(MX)]
for i in range(1, MX):
    for j in range(i * 2, MX, i):
        divisors[j].append(i)

def get_modify(s: str) -> int:
    res = n = len(s)
    for d in divisors[n]:
        cnt = 0
        for i0 in range(d):
            i, j = i0, n - d + i0
            while i < j:
                cnt += s[i] != s[j]
                i += d
                j -= d
        res = min(res, cnt)
    return res

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        modify = [[0] * n for _ in range(n - 1)]
        for left in range(n - 1):
            for right in range(left + 1, n):
                modify[left][right] = get_modify(s[left: right + 1])

        @cache
        def dfs(i: int, j: int) -> int:
            if i == 0:
                return modify[0][j]
            return min(dfs(i - 1, L - 1) + modify[L][j] for L in range(i * 2, j))
        return dfs(k - 1, n - 1)

