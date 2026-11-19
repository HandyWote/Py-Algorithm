class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()
        return min(nums[-3] - nums[0], nums[-2] - nums[1], nums[-1] - nums[2])


if __name__ == "__main__":
    s = Solution()
    print(s.minimizeSum([58,42,8,75,28]))
