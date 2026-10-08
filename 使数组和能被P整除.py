from itertools import accumulate


class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        s = list(accumulate(nums, initial=0))
        x = s[-1] % p
        if x == 0:
            return 0
        ans = n = len(nums)
        last = {}
        for i, v in enumerate(s):
            last[v % p] = i
            j = last.get((v - x) % p, -n)
            ans = min(ans, i-j)
        return ans if ans < n else -1

if __name__ == "__main__":
    cases = {
        'input': [
            ([3,1,4,2], 6),
            ([6,3,5,2], 9),
            ([1,2,3], 3),
            ([1,2,3], 7),
            ([1000000000,1000000000,1000000000], 3),
        ],
        'output': [
            1,
            2,
            0,
            -1,
            0,
        ]
    }
    from test import Test
    Test(cases, Solution(), 'minSubarray').run()