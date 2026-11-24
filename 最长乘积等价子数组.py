from math import gcd
class Solution:
    def maxLength(self, nums: list[int]) -> int:
        ans: int = 2
        mul: int = 1
        left: int = 0
        for right, x in enumerate(nums):
            while gcd(mul, x) > 1:
                mul //= nums[left]
                left += 1
            mul *= x
            ans = max(ans, right - left + 1)
        return ans

