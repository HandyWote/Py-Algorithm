class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        n: int = len(nums)
        target: int = sum(nums) // 2
        if sum(nums) & 1:
            return False
        dp: list[bool] = [False] * (target+1)
        dp[0] = True

        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
            if dp[target]:
                return True
        return dp[target]
        
if __name__ == "__main__":
    s = Solution()
    print(s.canPartition([1,5,11,5]))
