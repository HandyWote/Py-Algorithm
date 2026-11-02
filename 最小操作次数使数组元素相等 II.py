
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid: int = nums[len(nums)//2]
        return sum([abs(i-mid) for i in nums])

