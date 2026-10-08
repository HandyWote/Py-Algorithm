class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

def test():
    test_cases = {
        'case': [
            [3,7], [3,2], [7,3], [3,3]
        ],
        'expected': [
            28, 3, 28, 6
        ]
    }

    for i, case in enumerate(test_cases['case']):
        output = Solution().uniquePaths(*case)
        expected = test_cases['expected'][i]
        assert output == expected, f'case {i} failed: expected {expected}, got {output}'
        print(f'case {i} passed')

if __name__ == "__main__":
    test()