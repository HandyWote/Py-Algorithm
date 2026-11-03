class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return max(nums)*len(nums) - sum(nums)
