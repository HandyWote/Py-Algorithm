from cmath import inf
from itertools import accumulate
from pprint import pprint


class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        pre = list(accumulate(nums, initial=0))
        min_s = [inf] * k
        ans = -inf
        for j, s in enumerate(pre):
            i = j % k
            ans = max(ans, s - min_s[i])
            min_s[i] = min(min_s[i], s)
        return ans



if __name__ == "__main__":
    from test import Test
    cases = {
        'input': [
            ([1,2], 1),
            ([-1,-2,-3,-4,-5], 4),
            ([-5,1,2,-3,4], 2),
        ],
        'output': [
            3,
            -10,
            4,
        ]
    }
    Test(cases, Solution(), 'maxSubarraySum').run()