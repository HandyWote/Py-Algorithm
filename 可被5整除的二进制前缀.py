class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        ans = []
        n = ''
        for i in range(len(nums)):
            n += str(nums[i])
            temp = int(n, 2)
            ans.append(temp % 5 == 0)
        return ans

if __name__ == "__main__":
    cases = {
        'input': [
            [0,1,1],
            [1,1,1],
            [0,1,1,1,1,1],
            [1,1,1,0,1],
        ],
        'output': [
            [True,False,False],
            [False,False,False],
            [True,False,False,False,True,False],
            [False,False,False,False,False],
        ]
    }
    from test import Test
    Test(cases, Solution(), 'prefixesDivBy5').run()