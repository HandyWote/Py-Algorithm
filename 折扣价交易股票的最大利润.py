# 注意！这个写法很慢，更快的写法见写法二
max = lambda a, b: b if b > a else a

class Solution:
    def maxProfit(self, n: int, present: list[int], future: list[int], hierarchy: list[list[int]], budget: int) -> int:
        g = [[] for _ in range(n)]
        for x, y in hierarchy:
            g[x - 1].append(y - 1)

        def dfs(x: int) -> list[list[int]]:
            # 计算从 x 的所有儿子子树 y 中，能得到的最大利润之和（x 不买，x 买）
            sub_f = [[0, 0] for _ in range(budget + 1)]
            for y in g[x]:
                fy = dfs(y)
                for j in range(budget, -1, -1):
                    # 枚举子树 y 的预算为 jy
                    # 当作一个体积为 jy，价值为 fy[jy][k] 的物品
                    for jy in range(j + 1):  
                        for k in range(2):  # k=0 表示 x 不买，k=1 表示 x 买
                            sub_f[j][k] = max(sub_f[j][k], sub_f[j - jy][k] + fy[jy][k])

            # 计算从子树 x 中，能得到的最大利润之和（x 父节点不买，x 父节点买）
            f = [[0, 0] for _ in range(budget + 1)]
            for j in range(budget + 1):
                for k in range(2):  # k=0 表示 x 父节点不买，k=1 表示 x 父节点买
                    cost = present[x] // (k + 1)
                    if j >= cost:
                        # 不买 x，转移来源是 sub_f[j][0]
                        # 买 x，转移来源为 sub_f[j-cost][1]，因为对于子树来说，父节点一定买
                        f[j][k] = max(sub_f[j][0], sub_f[j - cost][1] + future[x] - cost)
                    else:  # 只能不买 x
                        f[j][k] = sub_f[j][0]
            return f

        return dfs(0)[budget][0]


if __name__ == '__main__':
    from test import Case, Test
    cases = Case(
        [
            ((2, [1,2], [4,3], [[1,2]], 3), 5),
            ((2, [3,4], [5,8], [[1,2]], 4), 4),
            ((3, [4,6,8], [7,9,11], [[1,2],[1,3]], 10), 10),
            ((3, [5,2,3], [8,5,6], [[1,2],[2,3]], 7), 12)
        ]
    )
    Test(cases, Solution(), 'maxProfit').run()