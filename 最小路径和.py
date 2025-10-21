class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = grid[i][0] + (dp[i - 1][0] if i > 0 else 0)
        for j in range(n):
            dp[0][j] = grid[0][j] + (dp[0][j - 1] if j > 0 else 0)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[m - 1][n - 1]


def test():
    cases = {
        'input': [
            ([[1,3,1],[1,5,1],[4,2,1]]),
            ([[1,2,3],[4,5,6]]),
        ],
        'output': [
            7,
            12,
        ]
    }
    solution = Solution()
    for i, case in enumerate(zip(cases['input'], cases['output'])):
        input_args, expected = case
        result = solution.minPathSum(input_args)
        assert result == expected, f"case {i} failed: expected {expected}, got {result}"
        print(f"case {i} passed")

if __name__ == "__main__":
    test()