class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        ans: list[int] = []
        nums.sort()
        for i, n in enumerate(nums):
            if n == target:
                ans.append(i)
        return ans


