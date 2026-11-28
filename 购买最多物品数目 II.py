
from collections import Counter

class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        items = self.pretake(items)
        items.sort(key= lambda x: x[0])
        limit: int = items[0][0] * 2
        ans: int = 0
        for price, gain in items:
            if price >= limit:
                break
            if gain <= 0:
                continue
            take: int = min(gain, budget // price)
            ans += 2 * take
            budget -= price * take
            if budget < price:
                break
        ans += budget//items[0][0]
        return ans
    
    @staticmethod
    def pretake(items: list[list[int]]) -> list[list[int]]:
        n: int = len(items)
        factor_cnt: Counter[int] = Counter([factor for factor, _ in items])
        gain: dict[int, int] = {}
        for factor, _ in items:
            total: int = 0
            if factor in gain:
                continue
            for j in range(factor, n+1, factor):
                total += factor_cnt.get(j, 0)
            gain[factor] = total - 1
        return [[price, gain[factor]] for factor, price in items]

if __name__ == "__main__":
    s = Solution()
    s.pretake([[1,6],[2,4],[3,5]])
    s.pretake([[2,8],[1,10],[6,6],[4,12],[5,20],[5,17]])
