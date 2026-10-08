class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(m):
            for j in range(n):
                for r in range(k):
                    if i > 0:
                        dp[i][j][(r + grid[i][j]) % k] = (dp[i][j][(r + grid[i][j]) % k] + dp[i-1][j][r]) % mod
                    if j > 0:
                        dp[i][j][(r + grid[i][j]) % k] = (dp[i][j][(r + grid[i][j]) % k] + dp[i][j-1][r]) % mod
        return dp[m-1][n-1][0]

class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7
        dp = [[0]*n for _ in range(m)]
        

if __name__ == "__main__":
    cases = {
        'input':[
            ([[5,2,4],[3,0,5],[0,7,2]], 3),
            ([[0,0]], 5),
            ([[7,3,4,9],[2,3,6,2],[2,3,7,0]], 1)
        ],
        'output':[
            2,
            1,
            10
        ]
    }
    from test import Test
    Test(cases, Solution(), 'numberOfPaths').run()
    