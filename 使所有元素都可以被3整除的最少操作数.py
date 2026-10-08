class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        ans = 0
        for i in nums:
            ans += min(i % 3, 3 - i % 3)
        return ans

if __name__ == "__main__":
    cases = {
        "input":[
            [1,2,3,4],
            [3,6,9]
        ],
        "output":[
            3,
            0
        ]
    }
    from test import Test
    Test(solution=Solution(), cases=cases, func='minimumOperations').run()