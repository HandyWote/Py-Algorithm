from functools import reduce
from operator import and_

class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        pool: list[int] = []
        for i, n in enumerate(nums):
            if i != n:
                pool.append(n)
        return reduce(and_, pool) if pool else 0
