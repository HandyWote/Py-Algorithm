class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        from math import inf
        f: list[int] = [0] * (budget + 1)
        min_price: float = inf

        for factor, price in items:
            min_price = min(min_price, price)

            cnt = 0
            for factor_j, _ in items:
                if factor_j % factor == 0:
                    cnt += 1

            for j in range(budget, price - 1, -1):
                f[j] = max(f[j], f[j - price] + cnt)

        return int(max(fi + (budget - i) // min_price for i, fi in enumerate(f)))

