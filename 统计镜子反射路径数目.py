from functools import cache


class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        @cache
        def dfs(i: int, j: int, k: int) -> int:
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1
            if grid[i][j] == 0:
                return (dfs(i, j - 1, 0) + dfs(i - 1, j, 1)) % 1_000_000_007
            if k == 0:
                return dfs(i - 1, j, 1)
            return dfs(i, j - 1, 0)

        m, n = len(grid), len(grid[0])
        return dfs(m - 1, n - 1, 0)
