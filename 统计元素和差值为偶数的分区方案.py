class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        ans = 0
        for i in range(1, len(nums)):
            if (sum(nums[:i]) - sum(nums[i:])) % 2 == 0:
                ans += 1
        return ans
    
class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        return len(nums) - 1 if sum(nums) % 2 == 0 else 0

if __name__ == "__main__":
    cases = {
        "input": [
            [10,10,3,7,6],
            [1,2,2],
            [2,4,6,8],
        ],
        "output": [
            4,
            0,
            3,
        ]
    }
    from test import Test
    Test(cases, Solution(), "countPartitions").run()