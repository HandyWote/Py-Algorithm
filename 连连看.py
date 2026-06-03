import sys
from collections import defaultdict
input = sys.stdin.readline

def get_input():
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    return n, m, a

def solve(n, m, a):
    # main_diag[i-j] = {值: 出现次数}
    main_diag = defaultdict(lambda: defaultdict(int))
    # anti_diag[i+j] = {值: 出现次数}
    anti_diag = defaultdict(lambda: defaultdict(int))

    for i in range(n):
        for j in range(m):
            val = a[i][j]
            main_diag[i - j][val] += 1
            anti_diag[i + j][val] += 1

    ans = 0
    # 主对角线配对
    for diag in main_diag.values():
        for cnt in diag.values():
            ans += cnt * (cnt - 1) // 2

    # 副对角线配对
    for diag in anti_diag.values():
        for cnt in diag.values():
            ans += cnt * (cnt - 1) // 2

    return ans * 2  # 顺序不同算不同对

if __name__ == "__main__":
    N, M, A = get_input()
    print(solve(N, M, A))