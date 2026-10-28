class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m: int = len(grid)
        n: int = len(grid[0])
        dp: list[list[set[int]]] = [[set() for _ in range(n)] for _ in range(m)]

        dp[0][0] = {grid[0][0]}
        for i in range(1, n):
            dp[0][i] = {x ^ grid[0][i] for x in dp[0][i - 1]}
        for i in range(1, m):
            dp[i][0] = {x ^ grid[i][0] for x in dp[i - 1][0]}

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = {x ^ grid[i][j] for x in dp[i - 1][j] | dp[i][j - 1]}

        return min(dp[-1][-1])
