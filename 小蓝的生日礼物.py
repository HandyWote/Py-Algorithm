from functools import lru_cache
import sys
sys.setrecursionlimit(100000)
card = [0,0,2,2,5,5,1,6]
sums = sum(card)
length = [0,0,0]
ans = set()

@lru_cache(maxsize=None)
def dfs(status, idx):  # 位记录状态 正在组成第几号边长
    if idx == 3:
        l = sorted(length)
        if l[0] + l[1] <= l[2]:
            ans.add(tuple(l))
        return
    if status + 1 == 1<<8:
        return
    for i in range(8):
        if not status & (1<<i):  # 可以选择
            dfs(status,idx+1)  # 不选就下一个
            length[idx] = 10*length[idx]+card[i]
            dfs(status|(1<<i),idx)  # 选

dfs(0,0)
print(len(ans))