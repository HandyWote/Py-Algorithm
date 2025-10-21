class Solution:
    def maxFrequency(self, nums: list[int], k: int, oprs: int) -> int:
        mn, mx = min(nums), max(nums)
        cnt = [0] * (mx + 1)
        for v in nums:
            cnt[v] += 1

        s = [0] * (mx + 2)
        for i, v in enumerate(cnt):
            s[i + 1] = s[i] + v

        ans = 0
        for v in range(mn, mx + 1):
            sz = s[min(mx + 1, v + k + 1)] - s[max(0, v - k)]
            ans = max(ans, min(cnt[v] + oprs, sz))
        return ans


def test():
    cases = {
        'input': [
            ([1,4,5], 1, 2),
            ([5,11,20,20], 5, 1),
        ],
        'output': [
            2,
            2,
        ]
    }
    solution = Solution()
    for i, case in enumerate(zip(cases['input'], cases['output'])):
        input_args, expected = case
        result = solution.maxFrequency(*input_args)
        assert result == expected, f"case {i} failed: expected {expected}, got {result}"
        print(f"case {i} passed")

if __name__ == "__main__":
    test()