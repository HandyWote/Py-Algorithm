class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        dp = [[0] * i for i in range(len(nums), 0, -1)]
        for i in range(len(nums)):
            dp[0][i] = nums[i]
        for i in range(1, len(nums)):
            for j in range(len(nums) - i):
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j + 1]) % 10
        return dp[-1][0]

if __name__ == "__main__":
    s = Solution()
    print(s.triangularSum([1,2,3,4,5]))  # Example test case