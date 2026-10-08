# 题目描述
# 小明冒充 X
# X星球的骑士，进入了一个奇怪的城堡。
# 城堡里边什么都没有，只有方形石头铺成的地面。
# 假设城堡地面是 n×n
# n×n 个方格。如下图所示。
# 按习俗，骑士要从西北角走到东南角。可以横向或纵向移动，但不能斜着走，也不能跳跃。每走到一个新方格，就要向正北方和正西方各射一箭。（城堡的西墙和北墙内各有n个靶子）同一个方格只允许经过一次。但不必走完所有的方格。如果只给出靶子上箭的数目，你能推断出骑士的行走路线吗？有时是可以的，比如上图中的例子。
# 本题的要求就是已知箭靶数字，求骑士的行走路径（测试数据保证路径唯一）
# 输入描述
# 第一行一个整数 
# N(0≤N≤20)，表示地面有 N×N 个方格。
# 第二行 
# N 个整数，空格分开，表示北边的箭靶上的数字（自西向东）
# 第三行 
# N 个整数，空格分开，表示西边的箭靶上的数字（自北向南）
# 输出描述
# 输出一行若干个整数，表示骑士路径。
# 为了方便表示，我们约定每个小格子用一个数字代表，从西北角开始编号: 0,1,2,3 

# 比如，上图中的方块编号为：

# 0 1 2 3

# 4 5 6 7

# 8 9 10 11

# 12 13 14 15

# 输入输出样例
# 示例
# 输入
# 4
# 2 4 3 4
# 4 3 3 3
# 输出
# 0 4 5 1 2 3 7 11 10 9 13 14 15

n = 4
n_list = [2, 4, 3, 4]
w_list = [4, 3, 3, 3]
from test import Case, Test

class Solution:
    @staticmethod
    def findWay(n: int, n_list: list[int], w_list: list[int]) -> str:
        north = n_list[:]
        west = w_list[:]

        path = []
        visited = [[False] * n for _ in range(n)]

        def dfs(r, c):
            visited[r][c] = True
            path.append(r * n + c)
            north[c] -= 1
            west[r] -= 1

            if r == n - 1 and c == n - 1 and all(x == 0 for x in north) and all(x == 0 for x in west):
                return True

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    if north[nc]>0 and west[nr]>0:
                        if dfs(nr, nc):
                            return True
            north[c] += 1
            west[r] += 1
            path.pop()
            visited[r][c] = False
            return False

        dfs(0, 0)
        return " ".join(map(str, path))

if __name__ == "__main__":
    s = Solution()
    cases = Case([
        ((4, [2, 4, 3, 4], [4, 3, 3, 3]), "0 4 5 1 2 3 7 11 10 9 13 14 15")
    ])
    Test(cases, s, "findWay").run()