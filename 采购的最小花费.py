class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        ans: int = 0
        if need1 > need2:
            ans += need2*min(cost1+cost2, costBoth) + (need1-need2)*min(cost1, costBoth)
        elif need2 > need1:
            ans += need1*min(cost1+cost2, costBoth) + (need2-need1)*min(cost2, costBoth)
        else:
            ans += need1*min(cost1+cost2, costBoth)
        return ans

