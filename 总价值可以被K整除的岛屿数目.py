class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m: int = len(grid)
        n: int = len(grid[0])
        ans: int = 0

        def dfs(i: int, j: int) -> int:
            value: int = 0
            if not(0 <= i < m and 0 <= j < n) or grid[i][j] == 0:
                return 0
            value += grid[i][j]
            grid[i][j] = 0
            for k in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                value += dfs(*k)
            return value
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if dfs(i, j) % k != 0:
                    continue
                ans += 1

        return ans

        

