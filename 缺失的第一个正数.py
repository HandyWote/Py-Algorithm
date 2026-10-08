from collections import defaultdict


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        d = defaultdict(int)
        for i, num in enumerate(nums):
            if num > 0:
                d[num] += 1
        for i in range(1, len(nums) + 2):
            if i not in d:
                return i
            
if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive([1,2,0]))  # Output: 3
    print(s.firstMissingPositive([3,4,-1,1]))  # Output: 2
    print(s.firstMissingPositive([7,8,9,11,12]))  # Output: 1