class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m: int = len(grid)
        n: int = len(grid[0])
        ans: int = 0
        row_count: list[int] = [0] * m
        col_count: list[int] = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row_count[i] += 1
                    col_count[j] += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] and (row_count[i] > 1 or col_count[j] > 1):
                    ans += 1

        return ans

if __name__ == '__main__':
    grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
    s = Solution()
    print(s.countServers(grid))
