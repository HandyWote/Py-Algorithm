class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        ans = len(prices)
        count = 1
        for i in range(1, len(prices)):
            if prices[i] + 1 == prices[i - 1]:
                count += 1
            else:
                count = 1
            ans += count - 1
        return ans 

if __name__ == "__main__":
    from test import Test, Case
    cases = Case(
        [
            ([3,2,1,4], 7),
            ([8,6,7,7], 4),
            ([1], 1),
        ]
    )
    Test(cases, Solution(), 'getDescentPeriods').run()