class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        dp: list[int] = [0 for _ in range(n+1)]
        dp[1] = costs[0] + 1
        if n > 1:
            dp[2] = costs[1] + min(dp[1]+1, dp[0]+4)
        for i in range(3, n+1):
            dp[i] = costs[i-1] + min(dp[i-1]+1, dp[i-2]+4, dp[i-3]+9)
        return dp[n]
