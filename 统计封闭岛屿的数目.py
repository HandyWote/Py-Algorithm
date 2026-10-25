class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        ans: int = 0
        rows: int = len(grid)
        cols: int = len(grid[0])

        def dfs(i: int, j: int) -> None:
            if not (0 <= i < rows and 0 <= j < cols) or grid[i][j] == 1:
                return
            grid[i][j] = 1
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            return

        for i in range(rows):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][cols - 1] == 0:
                dfs(i, cols - 1)

        for j in range(cols):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[rows - 1][j] == 0:
                dfs(rows - 1, j)


        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if grid[i][j] == 0:
                    ans += 1
                    dfs(i, j)

        return ans
