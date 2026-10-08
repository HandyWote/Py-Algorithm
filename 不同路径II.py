class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

def test():
    cases = {
        'input': [
            ([[0,0,0],[0,1,0],[0,0,0]]),
            ([[0,1],[0,0]]),
        ],
        'output': [
            2,
            1,
        ]
    }
    solution = Solution()
    for i, case in enumerate(zip(cases['input'], cases['output'])):
        input_args, expected = case
        result = solution.uniquePathsWithObstacles(input_args)
        assert result == expected, f"case {i} failed: expected {expected}, got {result}"
        print(f"case {i} passed")

if __name__ == "__main__":
    test()