class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        index = -1
        for i, n in enumerate(nums):
            if n == 1:
                if index != -1 and i - index - 1 < k:
                    return False
                index = i
        return True

if __name__ == "__main__":
    from test import test
    cases = {
            'input':[
                ([1,0,0,0,1,0,0,1], 2),
                ([1,0,0,1,0,1], 2,)
                ],
            'output': [
                True,
                False
            ]
        }
    s = Solution()
    t = test(cases, s, 'kLengthApart')
    t.run()