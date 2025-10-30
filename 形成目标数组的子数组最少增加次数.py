from itertools import pairwise


class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        ans = target[0]
        for x, y in pairwise(target):
            ans += max(y - x, 0)
        return ans
