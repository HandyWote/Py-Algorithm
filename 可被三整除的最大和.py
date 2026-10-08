from functools import cache
from math import inf


class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        @cache  # 记忆化搜索
        def dfs(i: int, j: int) -> int:
            if i < 0: return -inf if j else 0
            return max(dfs(i - 1, j), dfs(i - 1, (j + nums[i]) % 3) + nums[i])
        return dfs(len(nums) - 1, 0)


if __name__ == "__main__":
    cases = {
        'input':[
            [3,6,5,1,8],
            [4],
            [1,2,3,4,4]
        ],
        'output': [
            18,
            0,
            12
        ]
    }
    from test import Test
    Test(cases, Solution(), 'maxSumDivThree').run()