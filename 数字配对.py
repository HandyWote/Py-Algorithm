import sys
from collections import defaultdict
input = sys.stdin.readline

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

if __name__ == "__main__":
    N, A = get_input()
    pos = defaultdict(list)
    for i, x in enumerate(A):
        pos[x].append(i)
    maxv = max(A)
    del A
    end = {v: len(pos[v]) - 1 for v in pos}
    ans = 0
    for v in range(1, maxv):
        i = end.get(v, -1)
        j = end.get(v + 1, -1)
        if i < 0 or j < 0:
            continue
        P, Q = pos[v], pos[v + 1]
        while i >= 0 and j >= 0:
            if P[i] < Q[j]:
                ans += 1
                i -= 1
                j -= 1
            else:
                i -= 1
        end[v] = i
        end[v + 1] = j
    print(ans)
