from heapq import heappop, heappush
from math import inf


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dis = [[inf] * n for _ in range(n)]
        dis[0][0] = grid[0][0]
        h = [(grid[0][0], 0, 0)]  # 堆中保存 (起点到 (i,j) 的最少时间, i, j)

        while True:
            d, i, j = heappop(h)
            if i == j == n - 1:  # 到终点的最短路已确定
                return d
            if d > dis[i][j]:  # (i,j) 之前出堆过
                continue
            for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):  # 顺序无所谓，我们只看堆中最小的
                if 0 <= x < n and 0 <= y < n:
                    new_dis = max(d, grid[x][y])
                    if new_dis < dis[x][y]:
                        dis[x][y] = new_dis  # 更新 (i,j) 的邻居的最短路
                        # 懒更新堆：只插入数据，不更新堆中数据
                        # 相同节点可能有多个不同的 new_dis，除了最小的 new_dis，其余值都会触发上面的 continue
                        heappush(h, (new_dis, x, y))

if __name__ == "__main__":
    solution = Solution()
    grid = [[0, 2], [1, 3]]
    result = solution.swimInWater(grid)
    print(result)  # 输出: 3