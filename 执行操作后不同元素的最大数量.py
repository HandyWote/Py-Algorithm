from cmath import inf


class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        if k * 2 + 1 >= len(nums):
            return len(nums)
        nums.sort()
        ans = 0
        pre = -inf
        for x in nums:
            x = min(max(x - k, pre + 1), x + k)
            if x > pre:
                ans += 1
                pre = x
        return ans

def test():
    test_cases = {
        'case': [
            [[1,2,2,3,3,4], 2], [[4,4,4,4], 1], [[8,8,10,9,9], 1]
        ],
        'expected': [
            6, 3, 5
        ]
    }

    for i, case in enumerate(test_cases['case']):
        output = Solution().maxDistinctElements(*case)
        expected = test_cases['expected'][i]
        assert output == expected, f'case {i} failed: expected {expected}, got {output}'
        print(f'case {i} passed')

if __name__ == "__main__":
    test()