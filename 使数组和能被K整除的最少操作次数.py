class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        s = sum(nums)
        return s%k

if __name__ == "__main__":
    from test import Test
    cases = {
        "input": [
            ([3,9,7], 5),
            ([4,1,3], 4),
            ([3,2], 6),
        ],
        "output": [
            4,
            0,
            5,
        ]
    }
    Test(cases, Solution(), "minOperations").run()