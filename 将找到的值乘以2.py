

class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        unique = set(nums)
        while original in unique:
            original *= 2
        return original

if __name__ == "__main__":
    from test import test
    cases = {
        "input": [
            ([5,3,6,1,12], 3),
            ([2,7,9], 4),
        ],
        "output": [24, 4]
    }
    test(cases, Solution(), "findFinalValue").run()