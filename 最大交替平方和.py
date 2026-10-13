class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        length: int = len(nums)
        for i, x in enumerate(nums):
            nums[i] *= x
        nums.sort()
        
        return sum([x for x in nums[length//2:]] + [-x for x in nums[:length//2]])
