from functools import lru_cache
from math import ceil


class Solution:
    def minArraySum(self, nums: list[int], k: int, op1: int, op2: int) -> int:
        @lru_cache(None)
        def func(i: int, op1: int, op2:int) -> int:
            if i < 0:
                return 0
            x = nums[i]
            res = func(i-1, op1, op2) + x
            if op1 > 0:
                res = min(res, func(i-1, op1-1, op2) + ceil(x/2))
            if op2 > 0 and x >= k:
                res = min(res, func(i-1, op1, op2-1) + x - k)
                if op1:
                    y = (x + 1) // 2 - k if (x + 1) // 2 >= k else (x - k + 1) // 2
                    res = min(res, func(i - 1, op1 - 1, op2 - 1) + y)
            return res
        return func(len(nums) - 1, op1, op2)

if __name__ == "__main__":
    s = Solution()
    print(s.minArraySum([2,8,3,19,3], 3, 1, 1))