class Solution:
    def maxProfit(self, prices: list[int], strategy: list[int], k: int) -> int:
        half_k = k // 2
        n = len(strategy)
        profit_list = [p * s for p, s in zip(prices, strategy)]
        # 前缀和
        profit_prefix = [0] * (n + 1)
        prices_prefix = [0] * (n + 1)
        for i in range(n):
            profit_prefix[i + 1] = profit_prefix[i] + profit_list[i]
            prices_prefix[i + 1] = prices_prefix[i] + prices[i]
        base_profit = profit_prefix[n]
        ans = base_profit
        for i in range(n - k + 1):
            window_profit = profit_prefix[i + k] - profit_prefix[i]
            window_price = prices_prefix[i + k] - prices_prefix[i + half_k]
            candidate = base_profit - window_profit + window_price
            if candidate > ans:
                ans = candidate
        return ans
    
if __name__ == "__main__":
    from test import Test, Case
    cases = Case(
        [
            (([4,2,8], [-1,0,1], 2), 10),
            (([5,4,3], [1,1,0], 2), 9),
            (([5,8], [-1,-1], 2), 8),
            (([4,7,13], [-1,-1,0], 2), 9),
        ]
    )
    Test(cases, Solution(), "maxProfit").run()