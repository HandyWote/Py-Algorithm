class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        l, r = 0, sum(batteries) // n + 1
        while l + 1 < r:
            x = (l + r) // 2
            if n * x <= sum(min(b, x) for b in batteries):
                l = x
            else:
                r = x
        return l
    
    def maxRunTime2(self, n: int, batteries: list[int]) -> int:
        total = sum(batteries)
        batteries.sort(reverse=True)
        for b in batteries:
            if b * n <= total:
                return total // n
            total -= b
            n -= 1


if __name__ == "__main__":
    from test import Test
    cases = {
        "input": [
            (2, [1, 1, 1, 1]),
            (2, [3, 3, 3]),
        ],
        "output": [
            2,
            4,
        ]
    }
    Test(cases, Solution(), "maxRunTime2").run()