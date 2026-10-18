MOD: int = 10**9 + 7
from math import comb

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        return (self.count(nums) - 1) % MOD
    
    @staticmethod
    def count(nums: list[int]) -> int:
        if not nums:
            return 1
            
        root = nums[0]
        left_nums = [x for x in nums[1:] if x < root]
        right_nums = [x for x in nums[1:] if x > root]
            
        return (comb(len(left_nums) + len(right_nums), len(left_nums)) * Solution.count(left_nums) * Solution.count(right_nums)) % MOD
