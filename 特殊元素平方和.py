class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        n = len(nums)
        indexes:set[int] = set([0, n-1])
        for i in range(1, n-1):
            if n % i == 0:
                indexes.add(i)

        return sum([nums[i]**2 for i in indexes])




