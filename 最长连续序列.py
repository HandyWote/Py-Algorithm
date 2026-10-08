class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        ml = 0
        cl = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cl += 1
            elif nums[i] != nums[i - 1]:
                ml = max(ml, cl)
                cl = 1
        ml = max(ml, cl)
        return ml
