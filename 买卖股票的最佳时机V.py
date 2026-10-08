from cmath import inf
from functools import cache


class Solution:
    def maximumProfit(self, prices: list[int], k: int) -> int:
        @cache
        def dfs(i: int, j: int, end_state: int) -> int:
            if j < 0:
                return -inf
            if i < 0:
                return -inf if end_state else 0
            p = prices[i]
            if end_state == 0:
                return max(dfs(i - 1, j, 0), dfs(i - 1, j, 1) + p, dfs(i - 1, j, 2) - p)
            if end_state == 1:
                return max(dfs(i - 1, j, 1), dfs(i - 1, j - 1, 0) - p)
            return max(dfs(i - 1, j, 2), dfs(i - 1, j - 1, 0) + p)

        ans = dfs(len(prices) - 1, k, 0)
        dfs.cache_clear()
        return ans

if __name__ == "__main__":
    from test import Test, Case
    cases = Case(
        [
            (([1,7,9,8,2], 2), 14),
            (([12,16,19,19,8,1,19,13,9], 3), 36),
        ]
    )
    Test(cases, Solution(), "maximumProfit").run()