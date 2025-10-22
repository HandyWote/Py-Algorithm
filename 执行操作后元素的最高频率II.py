from collections import defaultdict


class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        cnt = defaultdict(int)
        diff = defaultdict(int)
        for x in nums:
            cnt[x] += 1
            diff[x]
            diff[x - k] += 1
            diff[x + k + 1] -= 1

        ans = sum_d = 0
        for x, d in sorted(diff.items()):
            sum_d += d
            ans = max(ans, min(sum_d, cnt[x] + numOperations))
        return ans

def test():
    cases = {
        'input': [
            ([1,4,5], 1, 2),
            ([5,11,20,20], 5, 1),
            ([999999997,999999999,999999999], 999999999, 2)
        ],
        'output': [
            2,
            2,
            3
        ]
    }
    solution = Solution()
    for i, input in enumerate(cases['input']):
        output = cases['output'][i]
        assert solution.maxFrequency(*input) == output
        print(f'case {i} passed')

if __name__ == '__main__':
    test()